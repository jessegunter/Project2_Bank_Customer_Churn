import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, balanced_accuracy_score, classification_report


def test():
    print('test')

def getColumnTransform():
    # define column categories
    categorical_columns = ['Geography', 'Gender']
    ordinal_columns = ['Card Type']
    numerical_columns = ['CreditScore',  'Age', 'Tenure', 'Balance','NumOfProducts', 'HasCrCard','IsActiveMember', 'EstimatedSalary','Satisfaction Score','Point Earned' ]
    #define the transform
    column_transform = ColumnTransformer(
    transformers=[
        ('One Hot Encode', OneHotEncoder(handle_unknown= "ignore"), categorical_columns),
        ('Ordinal Encode', OrdinalEncoder(categories=[['SILVER', 'GOLD', 'PLATINUM', 'DIAMOND']]), ordinal_columns),
        ('Scaling', StandardScaler(with_mean=False), numerical_columns)
    ])
    return column_transform

def getPipeline(classifier):
    column_transform = getColumnTransform()
    steps = [('Transform', column_transform),
             ("Scale", StandardScaler(with_mean=False)),
             ("Classifier", classifier)]
    pipeline = Pipeline(steps)
    return pipeline

def scoreModel(y_test, y_pred):
    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    balanced_accuracy = balanced_accuracy_score(y_test, y_pred)
    classification = classification_report(y_test, y_pred)
    print("Accuracy Score:", accuracy)
    print("Balanced accuracy Score:", balanced_accuracy)
    print("Classification Report:\n", classification)
    return {'accuracy_score': accuracy, 'balanced_accuracy_score': balanced_accuracy, 'classification_report': classification}

def processData(bank_customer_df, classifier):
    #define X and y
    X = bank_customer_df.drop(columns=[ 'RowNumber', 'CustomerId', 'Surname', 'Exited', 'Complain'])
    y = bank_customer_df['Exited']
    # split the training and testing data
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)
    #get a pipeline
    pipeline = getPipeline(classifier)
    #fit the pipeline
    pipeline.fit(X_train, y_train)
    #make predictions
    predictions = pipeline.predict(X_test)
    #evaluate the model
    results = scoreModel(y_test, predictions)
    return results