
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("data/Marketing_AB_Testing.csv")
df['converted'] = df['converted'].astype(int)
df['test group'] = df['test group'].map({'psa': 0, 'ad': 1})
df = pd.get_dummies(df, columns=['most ads day'], prefix='most ads day')

features = ['test group', 'total ads', 'most ads hour'] + [col for col in df.columns if col.startswith('most ads day_')]
X = df[features]
y = df['converted']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

log_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(class_weight='balanced', random_state=42))
])

log_pipeline.fit(X_train, y_train)

with open("model.pkl", "wb") as f:
    pickle.dump(log_pipeline, f)

with open("input_columns.pkl", "wb") as f:
    pickle.dump(X.columns.tolist(), f)

print("✅ Model and input columns saved successfully.")
