# Large-Scale Dataset Pruning with Dynamic Uncertainty for MNIST

## **Configuration:**
    - K := 10 Epochs
    - J := 5 Epochs

## **Datasets:**
    Trainset size: 48000
     - Subset size(75%): 36000
     - Subset size(50%): 24000
     - Subset size(10%): 4799
    Validationset size: 12000
    Teset size: 10000

## **Results:**

### Baseline (100% data):
    (Train Accuracy: 99.39%)
    Validation Accuracy: 98.15%
    Test Accuracy: 98.30%

---

### Random Subsampling (75% data):
    (Train Accuracy: 99.78%)
    Validation Accuracy: 98.38%
    Test Accuracy: 98.36%

### Pruning (75% data):
    (Train Accuracy: 99.85%)
    Validation Accuracy: 98.05%
    Test Accuracy: 97.80%

---

### Random Subsampling (50% data):
    (Train Accuracy: 99.60%)
    Validation Accuracy: 97.82%
    Test Accuracy: 97.79%

### Pruning (50% data):
    (Train Accuracy: 99.19%)
    Validation Accuracy: 98.54%
    Test Accuracy: 98.66%

---

### Random Subsampling (10% data):
    (Train Accuracy: 99.48%)
    Validation Accuracy: 95.64%
    Test Accuracy: 96.09%

### Pruning (10% data):
    (Train Accuracy: 100.00%)
    Validation Accuracy: 77.82%
    Test Accuracy: 78.48%


## **Analysis:**


MNIST might not be the right dataset for this:
    => Small and very easy to reach high accuracy
    => We are interested in small changes, e. g. 0.1% of 10000 samples (testset) are 10 samples