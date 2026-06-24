# Student Performance Prediction using Machine Learning

## Objective
Build machine learning models to predict whether a student will Pass or Fail based on demographic and academic attributes.

## Dataset
StudentsPerformance.csv

## Tasks Performed
- Loaded and explored the dataset
- Created Average Score feature
- Generated Pass/Fail target variable
- Encoded categorical features
- Split data into training and testing sets
- Trained:
  - Logistic Regression
  - Decision Tree
  - Random Forest
- Evaluated models using:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
- Applied 5-Fold Cross Validation
- Tuned Decision Tree hyperparameters
- Tuned Random Forest hyperparameters
- Plotted Learning Curve
- Compared model performances

## Results

| Model | Accuracy |
|---------|---------|
| Logistic Regression | 100.0% |
| Decision Tree | 98.5% |
| Random Forest | 99.5% |

## Conclusion
Logistic Regression achieved the best performance with perfect accuracy and classification metrics. The learning curve indicates strong generalization and minimal overfitting, making it the most effective model for this dataset.
