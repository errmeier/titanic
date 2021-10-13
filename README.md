# titanic
CSE 40647 Data Science Project

## Data Organization

Data is partitioned into test and train subsets.
The full data from Kaggle is located in train.csv and test.csv.
For numerical only data, use n_train.csv and n_test.csv (excludes fields name,
ticket, cabin, embarked).

Note that passenger ID is just used to identify training instances, it should
not be used as a feature in any models.
