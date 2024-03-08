# Algorithm 1: Dataset pruning with dynamic uncertainty.
# Input: Trainingset - trainloader, pruning ratio: pruning_ratio
# Required Model: net_pruning, traing epochs: epochs, uncertainty window: J

# To track uncertainty
uncertainty_window = np.zeros((train_size, J)) # Uncertainty window
uncertainty_EQ2 = np.zeros((train_size, epochs-J+1)) # Uncertainty according to Eq.2
uncertainty = np.zeros(train_size) # Overall uncertainty according to Eq.3

# for k = 0, · · · , K − 1 do
for epoch in range(epochs):
    total_loss = 0.0
    idx = 0
    
    # Sample a batch B ∼ T.
    # for (xi, yi) ∈ B do:
    for inputs, labels in tqdm(trainloader, desc=f'Epoch {epoch + 1}/{epochs}'):
        # Compute prediction P(yi, xi, θ) and loss ℓ(ϕθ(A(xi)), yi)
        outputs = net_pruning(inputs)
        loss = crit(outputs, labels)

        # Store window
        predicted_values = outputs[range(outputs.size(0)), labels]
        uncertainty_window[idx:idx+len(labels), epoch%J] = predicted_values.detach().numpy()
        idx += len(labels)

    # if k ≥ J then
        # Compute uncertainty Uk−J (xi) using Eq. 2
    if epoch >= J-1:
            U_epoch = np.std(uncertainty_window, ddof=1, axis=1)
            uncertainty_EQ2[:, epoch-J+1] = U_epoch

    # for (xi, yi) ∈ B do:
    for inputs, labels in tqdm(trainloader, desc=f'Epoch {epoch + 1}/{epochs}'):
        optimizer_pruning.zero_grad()

        # Update θ ← θ − η∇θL, where L =Σℓ(ϕθ(A(xi)),yi) / |B|
        outputs = net_pruning(inputs)
        loss = crit(outputs, labels)
        loss.backward()
        optimizer_pruning.step()
        total_loss += loss.item()

    average_loss = total_loss / subset_size
    print(f'Epoch {epoch + 1}/{epochs}, Average Loss: {average_loss:.4f}')

# for (xi, yi) ∈ T do
    # Compute dynamic uncertainty U(xi) using Eq. 3
uncertainty = np.mean(uncertainty_EQ2, axis=1)

# Sort T in the descending order of U(·)
sorted_indices = np.argsort(uncertainty)[::-1]

# S ← front (1 − r) × |T | samples in the sorted T
subset_indices = sorted_indices[:int(len(sorted_indices)*(1-pruning_ratio))]

# Output: Pruned dataset S
train_dynamic_uncertainty_subset = Subset(dataset=trainloader.dataset, indices=subset_indices)
