# Project 2 - Bank Customer Churn   

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [Data Processing](#data-processing)
- [File Structure](#file-structure)
- [Problems Encountered](#problems-encountered)
- [References](#references)
- [Team Members](#team-members)
- [License](#license)

## PROJECT DESCRIPTION   
 Bank Europe understands that it is expensive to bring on new customers.  Therefore, the bank is concerned with customer churn, that is, the number of customers who are closing accounts. The Artificial Intelligence and Data Team(AIDT) has been tasked to better understand what leads a customer to close an account with the bank. AIDT will develop predictive models that could be used to develop loyalty programs and retention campaigns targeted to reduce churn.   

## INSTALLATION   

1. Ensure you have Python 3.10 or higher installed.   
2. Clone this repository: `git clone https://github.com/jessegunter/Project2_Bank_Customer_Churn.git`   

## USAGE   

1. Run the project: `bank_customer_churn.ipynb`   

## DATA PROCESSING:   

1. Data Collection: Bank customer churn dataset was downloaded from kaggle at https://www.kaggle.com/datasets/barun2104/telecom-churn    

2. Data Exploration: One .csv file was read in and explored through the columns and info() methods.  The info() method revealed that there were no null values.  Additionally, unique values were reviewed for 'Geography' & 'Card type' columns.    

3. Data Cleanup:   
    - A pipeline is referenced that applies OneHotEncoder & OrdinalEncoder:   
	- OneHotEncoder was applied to columns 'Geography' & 'Gender'   
	- OrdinalEncoder was applied to the column 'Card Type'   
    - These models were created inside different Jupyter notebooks, each referencing the pipeline file: Logistic Regression, Support Vector Machines(SVM),  K-Nearest Neighbors(KNN), Decision Trees, Random Forest & XGBoost
    - Here are the Accuracy & Balanced Accuracy Scores of those models:

<p align="center">
  <img src="/Resources/results-grid.jpeg" />
</p>

## File Structure

The project follows the following structure:

Code language: Python (python)   
Project2_Bank_Customer_Churn/   
├─bank_customer_churn.ipynb   
├─utilities.ipynb   
├─SVM.ipynb   
├─knn.ipynb   
├─logistic_regression.ipynb   
├─xgboost.ipynb   
├─README.md   
└─Resources/   
  -Customer-Churn-Records.csv   
  -results-grid.jpeg   

## PROBLEMS ENCOUNTERED:   


## REFERENCES   
1. https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn/data    

2. https://bootcampspot.instructure.com/   

3. https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax   

## TEAM MEMBERS   
1. Rebecca Carr   
2. Jesse Gunter   
3. Marianne Mittelstadt   
4. Steve Vierling   

## LICENSE   
This project is licensed under the Churn Busters      
