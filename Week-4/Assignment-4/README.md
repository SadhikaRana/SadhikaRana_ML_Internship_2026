# Loan Prediction using Machine Learning

## Overview
This project predicts whether a loan application will be approved or not using Machine Learning classification techniques. The dataset was preprocessed, analyzed, and used to train multiple models for loan approval prediction.

## Objectives
- Perform data preprocessing and cleaning.
- Handle missing values.
- Convert categorical features into numerical format.
- Train and evaluate Machine Learning models.
- Compare model performance using multiple evaluation metrics.
- Apply cross-validation and hyperparameter tuning.
- Analyze underfitting and overfitting behavior.

## Dataset Features
The dataset contains applicant information such as:
- Gender
- Marital Status
- Dependents
- Education
- Self Employment Status
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

### Target Variable
- **Loan_Status**
  - Approved (Y)
  - Not Approved (N)

## Data Preprocessing
- Missing value treatment
- Categorical variable encoding
- Feature scaling (if required)
- Feature and target selection

## Models Used
1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

## Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1 Score

## Advanced Techniques
- Stratified 5-Fold Cross Validation
- Hyperparameter Tuning using GridSearchCV
- Learning Curve Analysis
- Bias-Variance Analysis

## Key Findings
- Compared multiple classification algorithms.
- Evaluated model stability using cross-validation.
- Tuned Random Forest parameters for improved performance.
- Analyzed underfitting and overfitting using different Decision Tree depths.
- Identified the model with the best balance between bias and variance.

## Conclusion
Machine Learning techniques were successfully applied to predict loan approval status. Multiple models were trained and compared, and the best-performing model was selected based on evaluation metrics and cross-validation results.
