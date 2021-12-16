# titanic
CSE 40647 Data Science Project

## File Structure

### Data
The raw data files as well as the processed data files are in the data folder.
As mentioned below, the 5 different train and test subsets are labeled a through e.
The "n_train" and "n_test" files refer to pre-milestone when holdout validation (80%/20% split)
was used. The "kaggle_train" and "kaggle_test" are the raw data files downloaded from Kaggle.

### Code
The code used to preprocess the data as well as generate the models and the graphs are found in the src folder. 
The maiin python file to generate the models is the python notebook "titanic.pynb" which was produced using Colab.




## Data Organization

Data is partitioned into 5 different test and train subsets (a, b, c, d, e train and test).
The full, raw data from Kaggle is located in kaggle_train.csv and kaggle_test.csv.
The labeled data was split into n_train.csv and n_test.csv (excludes fields name,
ticket, cabin, embarked), and any rows with missing features were also excluded.

Note that passenger ID is just used to identify training instances, it should
not be used as a feature in any models.
