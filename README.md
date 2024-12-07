# Project 2 - Bank Customer Churn   

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [Data Processing](#data-processing)
- [File Structure](#file-structure)
- [Problems Encountered](#problems-encountered)
- [License](#license)
- [Credits](#credits)
- [Contact Information](#contact-information)
- [Additional Reading](#additional-reading)

## PROJECT DESCRIPTION   
 Bank Europe understands that it is more expensive to bring on new customers and is concerned with customer churn, the number of customers who are closing accounts. The Artificial Intelligence and Data Team has been tasked to better understand what leads a customer to close an account with the bank and develop predictive models that could be used to develop loyalty programs and retention campaigns targeted to reduce churn.   

## INSTALLATION   

1. Ensure you have Python 3.10 or higher installed.   
2. Clone this repository: `git clone https://github.com/jessegunter/Project2_Bank_Customer_Churn.git`   

## USAGE   

1. Run the project: `bank_customer_churn.ipynb`   

## DATA PROCESSING:   

1. Data Collection: Bank customer churn dataset was downloaded from kaggle at https://www.kaggle.com/datasets/barun2104/telecom-churn    

2. Data Exploration: One .csv file was read in and explored through the columns and info() methods.  The info() method revealed that there were no null values.  Additionally, unique values were reviewed for 'Geography' & 'Card type' columns.    

3. Data Cleanup:   
    - OneHotEncoder was applied to columns 'Geography' & 'Gender'   
    - OrdinalEncoder was applied to the column 'Card Type'   

### PROBLEMS ENCOUNTERED:   


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
