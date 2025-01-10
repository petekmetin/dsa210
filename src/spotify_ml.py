import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

# Function to preprocess data for ML
def prepare_data_for_ml(spotify_data):
    """Prepare features and target for machine learning."""
    # Select features and target
    features = spotify_data[['hoursPlayed', 'days_to_exam']].dropna()
    target = spotify_data.loc[features.index, 'stress_label'].map({'Non-Stress': 0, 'Stress': 1})
    
    # Scale features
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    
    return features_scaled, target

# Function to train and evaluate the ML model
def train_and_evaluate(features, target):
    """Train a classifier and evaluate its performance."""
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    
    # Train the model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    return model

# Main function
def main_with_ml():
    # Load processed Spotify data
    spotify_data = pd.read_csv("Processed_Spotify_Data.csv")
    
    # Prepare data for ML
    features, target = prepare_data_for_ml(spotify_data)
    
    # Train and evaluate the model
    model = train_and_evaluate(features, target)
    
    # Feature importance (optional)
    feature_importances = model.feature_importances_
    print("\nFeature Importances:")
    for feature, importance in zip(['hoursPlayed', 'days_to_exam'], feature_importances):
        print(f"{feature}: {importance:.4f}")

# Run the script with ML
if __name__ == "__main__":
    main_with_ml()
