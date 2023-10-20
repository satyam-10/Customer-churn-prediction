# Customer-churn-prediction
**1. Data Loading:**
- The code starts by loading a dataset from an Excel file containing customer information, including features like age, subscription length, monthly bill, total usage, gender, location, and the target variable 'Churn' (indicating whether a customer has churned or not).

**2. Exploratory Data Analysis:**
- The code performs some basic exploratory data analysis (EDA) to understand the dataset:
  - Checking for missing values (null values).
  - Descriptive statistics for numeric features.
  - Data visualization using various plots:
    - A pie chart to show the distribution of churn (target variable).
    - A bar plot to visualize the churn rate by gender.
    - Histogram for the 'Age' feature.
    - Box plots for subscription length, monthly bill, and total usage.
    - A heatmap to visualize the correlation between numeric features.

**3. Data Preprocessing:**
- Data preprocessing involves:
  - One-hot encoding for categorical features like 'Location' and 'Gender.'
  - Dropping unnecessary columns like 'CustomerID' and 'Name.'
  - Scaling numeric features using Min-Max scaling to bring them to a common scale between 0 and 1.

**4. Model Building:**
- Two machine learning models are built and evaluated:
  - **Logistic Regression:** A simple classification model.
  - **Random Forest Classifier:** A more complex ensemble model.
- The code uses the scikit-learn library for model building and evaluation.
- The models are trained and evaluated using metrics such as accuracy, precision, recall, and F1-score.

**5. Model Evaluation:**
- Model evaluation includes calculating various performance metrics:
  - Accuracy: The proportion of correctly classified instances.
  - Precision: The ability to avoid false positives.
  - Recall: The ability to avoid false negatives.
  - F1-Score: A metric that balances precision and recall.
- The code also prints the confusion matrix for model evaluation.

Overall, this code demonstrates the entire process of building and evaluating a customer churn prediction model, including data loading, exploratory data analysis, data preprocessing, and model building. It assesses two models' performance and provides important metrics for model evaluation.

## Streamlit App

1. **Data Input:** The app collects the following user information using input widgets:
   - Age: A slider to select the user's age.
   - Subscription Length: A slider to choose the subscription length in months.
   - Monthly Bill: A numeric input field for the monthly bill amount.
   - Total Usage (GB): A numeric input field for the total data usage in gigabytes.
   - Gender: A dropdown list to select the user's gender.

2. **Data Processing:** The app maps the selected gender to a numeric value for model input.

3. **Churn Prediction:** Upon clicking the "Predict Churn" button, the app uses the user's input data to make a churn prediction using a pre-trained machine learning model. If the model predicts no churn, it displays a success message with a low churn probability. If churn is predicted, it shows an error message with a high churn probability.

4. **Running the App:** The app can be run using the `streamlit run` command in the terminal. It opens a web page where users can interact with the app.

This Streamlit app simplifies the process of collecting user data and making churn predictions, making it a user-friendly tool for instructors or users interested in exploring the customer churn prediction model.
