import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta
import os
import seaborn as sns

# Function to load Spotify and exam data
def load_data(spotify_files, exam_file):
    """Load Spotify JSON files and Exam CSV file."""
    # Combine all Spotify JSON files
    spotify_data = pd.concat([pd.read_json(file) for file in spotify_files], ignore_index=True)
    # Load exam data
    exam_data = pd.read_csv(exam_file)
    exam_data['exam_date'] = pd.to_datetime(exam_data['exam_date'])
    return spotify_data, exam_data

# Function to preprocess data
def preprocess_data(spotify_data, exam_data):
    """Preprocess Spotify and Exam Data."""
    # Convert endTime to datetime and calculate hours played
    spotify_data['endTime'] = pd.to_datetime(spotify_data['endTime'])
    spotify_data['hoursPlayed'] = spotify_data['msPlayed'] / (1000 * 60 * 60)  # Convert ms to hours

    # Define stress periods
    exam_data['start_stress'] = exam_data['exam_date'] - timedelta(days=3)
    exam_data['end_stress'] = exam_data['exam_date'] + timedelta(days=3)

    # Label stress vs non-stress periods
    def label_stress(row, stress_periods):
        for _, period in stress_periods.iterrows():
            if period['start_stress'] <= row['endTime'] <= period['end_stress']:
                return 'Stress'
        return 'Non-Stress'

    spotify_data['stress_label'] = spotify_data.apply(
        lambda row: label_stress(row, exam_data[['start_stress', 'end_stress']]), axis=1
    )

    # Calculate days to nearest exam
    def days_to_exam(row, exam_dates):
        differences = (exam_dates - row['endTime']).dt.days
        future_differences = differences[differences >= 0]
        return future_differences.min() if not future_differences.empty else None

    spotify_data['days_to_exam'] = spotify_data.apply(
        lambda row: days_to_exam(row, exam_data['exam_date']), axis=1
    )

    return spotify_data, exam_data

# Function to analyze and visualize data
def analyze_and_visualize(spotify_data):
    """Generate visualizations for Spotify Data."""
    # Total listening hours by stress label
    stress_counts = spotify_data.groupby('stress_label')['hoursPlayed'].sum()

    # Bar plot: Stress vs Non-Stress listening hours
    plt.figure(figsize=(8, 6))
    stress_counts.plot(kind='bar', color=['blue', 'orange'])
    plt.title('Total Listening Hours: Stress vs. Non-Stress Periods')
    plt.ylabel('Total Hours Played')
    plt.xlabel('Stress Label')
    plt.xticks(rotation=0)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig("Total_Stress_NonStress_Comparison.png")
    plt.show()

    # Scatter plot: Days to exam vs listening activity
    days_to_exam_activity = spotify_data.groupby('days_to_exam')['hoursPlayed'].sum().reset_index()
    plt.figure(figsize=(10, 6))
    plt.scatter(days_to_exam_activity['days_to_exam'], days_to_exam_activity['hoursPlayed'], color='green')
    plt.title('Days to Exam vs. Listening Activity')
    plt.xlabel('Days to Exam')
    plt.ylabel('Total Hours Played')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("Days_to_Exam_vs_Activity.png")
    plt.show()

    # Heatmap: Correlation between numerical variables
    # Map stress_label to binary values for correlation (Non-Stress = 0, Stress = 1)
    spotify_data['stress_binary'] = spotify_data['stress_label'].map({'Non-Stress': 0, 'Stress': 1})
    correlation_data = spotify_data[['hoursPlayed', 'days_to_exam', 'stress_binary']].dropna()

    # Compute the correlation matrix
    corr_matrix = correlation_data.corr()

    # Create the heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("Correlation_Heatmap.png")
    plt.show()

# Main function to execute the script
def main():
    # File paths (update these paths based on your setup)
    spotify_files = [
        "/Users/petekmetin/Desktop/StreamingHistory_music_0.json",
        "/Users/petekmetin/Desktop/StreamingHistory_music_1.json",
        "/Users/petekmetin/Desktop/StreamingHistory_music_2.json",
        "/Users/petekmetin/Desktop/StreamingHistory_music_3.json",
        "/Users/petekmetin/Desktop/StreamingHistory_music_4.json",
    ]
    exam_file = "/Users/petekmetin/Desktop/exam_dates_sorted.csv"

    # Check if files exist
    for file in spotify_files + [exam_file]:
        if not os.path.exists(file):
            print(f"Error: File not found: {file}")
            return

    # Load data
    spotify_data, exam_data = load_data(spotify_files, exam_file)

    # Preprocess data
    spotify_data, exam_data = preprocess_data(spotify_data, exam_data)

    # Save processed data
    spotify_data.to_csv("Processed_Spotify_Data.csv", index=False)
    exam_data.to_csv("Processed_Exam_Data.csv", index=False)

    # Analyze and visualize
    analyze_and_visualize(spotify_data)

# Run the script
if __name__ == "__main__":
    main()
