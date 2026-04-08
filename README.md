# Adult Income Dataset - Exploratory Data Analysis (EDA)

##  Project Overview

This project conducts Exploratory Data Analysis (EDA) on the Adult Income dataset. The main objectives are to:

- Analyze the dataset’s structure and key features
- Identify and address missing values
- Perform data cleaning
- Re-run the analysis after cleaning to observe any changes


The dataset aims to predict whether an individual’s income exceeds $50K per year, with the target variable having two categories:

<=50K OR >50K



##  Dataset 

The dataset contains demographic and employment-related attributes such as: 

- Age 
- Workclass 
- Education 
- Occupation 
- Hours per week 
- Native country 
- Income 

The dataset consists of 48,842 rows and 15 columns after combining training and test data.



## Exploratory Data Analysis (EDA)

### 1. Basic Analysis

- Loaded Datasets: Imported both adult.data (training set) and adult.test (test set).
- Cleaned Test Dataset: Performed necessary cleaning on the test data to ensure consistency with the training set.
- Combined Data: Merged the cleaned training and test datasets into a single dataframe for unified analysis.
- Initial Data Exploration: Examined the combined dataset’s structure, checked data types, and reviewed summary statistics to understand distributions and detect anomalies.



### 2. Detect Missing Values

Missing values were detected using: **df.isnull().sum()**

The following columns contain missing values:

Column           Missing Count
  
Occupation       2809

Workclass        2799

Native_country   857



### 3. Quantify Missing Data

Missing data percentages:

Column           Percentage

occupation       5.75%

workclass        5.73%

native_country   1.75%


## Handling Missing Data

The chosen method for handling missing data was **df.dropna()**

### Reason:

- Low Percentage of Missing Data: The proportion of missing values in the dataset is relatively small.
- Sufficient Dataset Size: The dataset is large enough that removing rows with missing values will not lead to a significant loss of information.
- Simplicity and Bias Avoidance: This removal approach is straightforward and helps avoid introducing bias that could result from imputation or other complex methods.

### Alternative Approach (Imputation)

Another possible method would be **imputation**, where missing values are replaced instead of removed.

For example: **df\["workclass"\].fillna(df\["workclass"\].mode()\[0\],inplace=True)**

### Why it was not chosen:

- Risk of Bias: Imputation can introduce bias by over-representing the most common category or value.
- Distortion of Distribution: Filling in missing values may distort the true distribution of the data, potentially affecting analysis and model performance.
- Sufficiency of Row Removal: Given the large dataset size and low percentage of missing data, simply dropping rows with missing values was sufficient and more appropriate for this project.

### 5. Re-running EDA After Cleaning

After removing missing values: 
- Dataset size reduced to 45,222rows
- All missing values were successfully removed

## Data Visualization

Generated plots: 

- Income Distribution 
- Age Distribution 
- Hours per Week Distribution

## Testing

Tests implemented using pytest.

### Passing Tests

-   Dataset loads correctly
-   Missing values detected correctly
-   Cleaning removes missing values

### Failing Tests 

-   Incorrect dataset shape
-   No missing values before cleaning

Expected result: 3 passed, 2 failed


