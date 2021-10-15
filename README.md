# titanic
CSE 40647 Data Science Project

## Data Organization

Data is partitioned into test and train subsets.
The full, raw data from Kaggle is located in kaggle_train.csv and kaggle_test.csv.
The labeled data was split into n_train.csv and n_test.csv (excludes fields name,
ticket, cabin, embarked), and any rows with missing features were also excluded.

Note that passenger ID is just used to identify training instances, it should
not be used as a feature in any models.
