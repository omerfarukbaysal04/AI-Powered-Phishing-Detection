import pandas as pd
import joblib

#Github:@omerfarukbaysal04

# 1. Upload model and vectorizer files
model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# 2. Request a file path from the user
file_path = input("Enter the name of the Excel file to be tested (e.g. test_data.xlsx): ")

try:
    # 3. Read file
    df = pd.read_excel(file_path)

    # 4. Select the URL column for the prediction
    X_test_urls = df["URL"]

    # 5. Make URLs digital with vectorizer
    X_test_vectorized = vectorizer.transform(X_test_urls)

    # 6. Make a prediction
    predicts = model.predict(X_test_vectorized)

    # 7. Add and show the results to Dataframe
    df["Predict"] = predicts
    print("\nPredicted URLs:")
    print(df)

    print("\nPrediction complated ✅")

except FileNotFoundError:
    print(f"Error: '{file_path}' didn't find. Please try again.")
except KeyError:
    print("Error: The file could not find a column named 'URL'. Please check the column name.")