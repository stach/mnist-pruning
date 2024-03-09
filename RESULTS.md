# Large-Scale Dataset Pruning with Dynamic Uncertainty for MNIST

## **Configuration:**
    - K := 10 Epochs
    - J := 5 Epochs
    - Train Epochs: 
        - 10 with lr 0.001 and AdamW
        - 10 with lr 0.0001 and AdamW
        => Training epochs

## **Datasets:**
    Trainset size: 48000
     - Subset size(75%): 36000
     - Subset size(50%): 24000
     - Subset size(10%): 4799
    Validationset size: 12000
    Teset size: 10000

## **Results:**

### Baseline (100% data):
    (Train Accuracy: 99.52%)
    Validation Accuracy: 98.48%
    Test Accuracy: 98.70%

---

### Random Subsampling (75% data):
    (Train Accuracy: 99.59%)
    Validation Accuracy: 98.49%
    Test Accuracy: 98.61%


### Pruning (75% data):
    (Train Accuracy: 99.41%)
    Validation Accuracy: *98.60%
    Test Accuracy: *98.63%

---

### Random Subsampling (50% data):
    (Train Accuracy: 99.45%)
    Validation Accuracy: 97.97%
    Test Accuracy: 98.33%


### Pruning (50% data):
    Train Accuracy: 99.05%
    Validation Accuracy: *98.25%
    Test Accuracy: *98.44%


---

### Random Subsampling (5% data):
    (Train Accuracy: 96.88%)
    Validation Accuracy: *92.66%
    Test Accuracy: *93.26%

### Pruning (5% data - 10x the number of epochs):
    (Train Accuracy: 93.42%)
    Validation Accuracy: 91.10%
    Test Accuracy: 92.23%


# **Observation:**

Convergence behavior seems more complex for the pruning Approach

MNIST might not be the right dataset for this:
    => Small and very easy to reach high accuracy
    => We are interested in small changes, e. g. 0.1% of 10000 samples (testset) are 10 samples