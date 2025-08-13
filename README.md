

### README.md


# Phishing URL Detector

## About the Project

This project is a Python application that detects malicious (phishing) URLs using artificial intelligence and machine learning. The project uses a **Random Forest Classifier** model to predict whether a URL is a phishing site or not. The model is trained on a labeled dataset and can classify new, unknown URLs with a high degree of accuracy.

## Technologies Used

* **Python:** The main programming language for the project.
* **Pandas:** Used for loading and processing the dataset.
* **Scikit-learn:** Provides the machine learning model (**Random Forest**) and data preprocessing tools (**CountVectorizer**).
* **Joblib:** Used to save and load the trained model and the vectorizer.

## Setup

To get a local copy up and running, follow these simple steps:

1.  Clone the repository:
    ```bash
    git clone [https://github.com/omerfarukbaysal04/Phishing-URL-Detector.git](https://github.com/omerfarukbaysal04/Phishing-URL-Detector.git)
    cd Phishing-URL-Detector
    ```

2.  Install the required libraries from the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Training the Model

To train the model, run the `train.py` script. This command will use the data in `MyDataSET.xlsx` to create a model, which will be saved as `phishing_model.pkl` and `vectorizer.pkl`.

```bash
python src/train.py
````

### 2\. Making Predictions

To make predictions on new URLs using the trained model, run the `predict.py` script. The script will prompt you to enter the name of the Excel file you want to test.

```bash
python src/predict.py
```

For example, after running the script, you would enter a filename like `test_data.xlsx` to make predictions.

-----

## Dataset

The project uses an Excel file (`MyDataSET.xlsx`) containing two columns: 'URL' and 'ClassLabel'. The `ClassLabel` column holds the values `0` for phishing URLs and `1` for safe URLs.

-----

## Author

  * **Ömer Faruk Baysal** - [omerfarukbaysal04](https://www.google.com/search?q=https://github.com/omerfarukbaysal04)

<!-- end list -->

```
```
