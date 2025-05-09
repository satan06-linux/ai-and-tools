import pandas as pd  ## pip install pandas ##
from sklearn.model_selection import train_test_split ## pip install sklearn ##
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

# Sample data with skills as categorical
data = {
    '10th_percentage': [85, 78, 90, 65, 88, 70, 95, 60],
    '12th_percentage': [80, 75, 92, 60, 85, 68, 96, 58],
    'degree_percentage': [75, 70, 88, 55, 80, 65, 90, 50],
    'internship': [1, 0, 1, 0, 1, 0, 1, 0],  # 1 if done internship, else 0
    'skills': ['Python', 'Java', 'Python', 'C++', 'Java', 'C++', 'Python', 'Java'],
    'selected': [1, 0, 1, 0, 1, 0, 1, 0]  # 1 if selected, else 0
}

df = pd.DataFrame(data)

# Features and target
X = df.drop('selected', axis=1)
y = df['selected']

# Define categorical and numerical columns
categorical_features = ['skills']
numerical_features = ['10th_percentage', '12th_percentage', 'degree_percentage', 'internship']

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Create pipeline with preprocessing and model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Real-time prediction function
def predict_selection(input_data):
    """
    input_data: dict with keys '10th_percentage', '12th_percentage', 'degree_percentage', 'internship', 'skills'
    """
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    return "Selected" if prediction[0] == 1 else "Not Selected"

# Example real-time prediction
new_candidate = {
    '10th_percentage': 82,
    '12th_percentage': 78,
    'degree_percentage': 80,
    'internship': 1,
    'skills': 'Python'
}

result = predict_selection(new_candidate)
print("Real-time prediction:", result)
