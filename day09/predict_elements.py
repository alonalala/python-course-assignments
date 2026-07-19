import os
import pandas as pd
import urllib.request
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

def download_data():
    """Downloads the E. coli promoter dataset from the UCI repository."""
    # Fixed the missing hyphen in 'promoter-gene-sequences'
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/promoter-gene-sequences/promoters.data"
    file_path = "promoters.data"

    if not os.path.exists(file_path):
        print("Downloading dataset from UCI Machine Learning Repository...")
        urllib.request.urlretrieve(url, file_path)
        print("Download complete.\n")
    else:
        print("Dataset already exists locally.\n")

    return file_path

def process_data(file_path):
    """Loads the data and extracts sequence grammar features."""
    # The dataset has 3 columns: Class (+ or -), Instance Name, and the DNA Sequence
    df = pd.read_csv(file_path, header=None, names=['Class', 'ID', 'Sequence'])

    # Clean up the sequence strings (remove whitespace/tabs)
    df['Sequence'] = df['Sequence'].str.strip().str.upper()

    # Feature Engineering: Extract basic sequence grammar metrics
    print("Extracting sequence features...")
    df['Length'] = df['Sequence'].apply(len)
    df['A_count'] = df['Sequence'].apply(lambda x: x.count('A'))
    df['T_count'] = df['Sequence'].apply(lambda x: x.count('T'))
    df['G_count'] = df['Sequence'].apply(lambda x: x.count('G'))
    df['C_count'] = df['Sequence'].apply(lambda x: x.count('C'))
    df['GC_content'] = ((df['G_count'] + df['C_count']) / df['Length']) * 100
    df['CpG_count'] = df['Sequence'].apply(lambda x: x.count('CG'))

    # Convert target class to binary (1 for promoter '+', 0 for non-promoter '-')
    df['Target'] = df['Class'].apply(lambda x: 1 if x.strip() == '+' else 0)

    return df

def run_prediction():
    # 1. Get and process data
    file_path = download_data()
    data = process_data(file_path)

    # 2. Define Features (X) and Target (y)
    feature_columns = ['A_count', 'T_count', 'G_count', 'C_count', 'GC_content', 'CpG_count']
    X = data[feature_columns]
    y = data['Target']

    # 3. Split into training and testing sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Train a Random Forest Classifier
    print("Training Random Forest Classifier...\n")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 5. Make predictions and evaluate
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print("--- Model Evaluation ---")
    print(f"Accuracy: {accuracy * 100:.2f}%\n")
    print("Classification Report:")
    print(classification_report(y_test, predictions, target_names=['Non-Promoter', 'Promoter']))

    # 6. Feature Importance
    print("--- Sequence Feature Importance ---")
    importances = model.feature_importances_
    for feature, imp in zip(feature_columns, importances):
        print(f"{feature}: {imp:.4f}")

# Fixed the entry point syntax here
if __name__ == "__main__":
    run_prediction()
