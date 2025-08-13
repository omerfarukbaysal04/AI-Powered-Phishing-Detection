import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
from sklearn.feature_extraction.text import CountVectorizer

#Github:@omerfarukbaysal04

# 1. Upload dataset
data_frame = pd.read_excel("MyDataSET.xlsx") #example dataset

# 2. Özellik ve hedef
X = data_frame["URL"]           # URLs
y = data_frame["ClassLabel"]    # Target column

# 3. Convert url to number
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# 4. Divide by training and test data
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# 5. Create and train a model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 6. Make a prediction and calculate accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy rate: {accuracy * 100:.2f}%")

# 7. Save model and vectorizer
joblib.dump(model, "phishing_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("Model and vectorizer saved ✅")
