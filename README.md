# Spotify Exam Analysis

**Sabancı University DSA210 Introduction to Data Science Course Fall 2024-2025 Term Project**
** Petek Metin (32627)

This project explores the relationship between my Spotify listening habits and exam dates to analyze how music preferences might correlate with stress and study habits. By examining genres, artists, and listening patterns, I aim to uncover trends in my behavior during high-stress periods.

## Table of Contents
1. [Motivation](#motivation)
2. [Main Research Questions](#main-research-questions)
3. [Data](#data)
4. [Methodology](#methodology)
5. [Findings](#findings)
6. [Limitations](#limitations)
7. [Future Work](#future-work)
8. [How to Run the Code](#how-to-run-the-code)
9. [Repository Structure](#repository-structure)

## Motivation

Music often reflects emotional states, and stress periods like exams may influence listening habits. This project aims to understand how my music preferences change during high-stress times, particularly leading up to exams.

## Main Research Questions

1. How do my listening habits change in the days leading up to and following exams?
2. Are there specific genres, artists, or moods I favor during high-stress periods?
3. Is there a measurable correlation between days-to-exam and listening activity?

## Data

### Spotify Data
- **Source**: Exported using Spotify's data download feature.
- **Contents**: Listening history, including timestamps, track names, artists, and playback duration.

### Exam Dates
- **Source**: Manually compiled.
- **Contents**: Specific dates and times of exams for the semester.

All data files are stored in the `data/` folder.

## Methodology

1. **Preprocessing**:
   - Combined multiple Spotify JSON files into a single dataset.
   - Added a `days_to_exam` feature to link listening activity to stress periods.
2. **Exploratory Data Analysis (EDA)**:
   - Analyzed total listening hours, genre distribution, and time-of-day patterns.
   - Compared stress and non-stress periods.
3. **Correlation Analysis**:
   - Investigated relationships between listening hours and days-to-exam.
4. **Visualization**:
   - Created bar charts, line graphs, scatter plots, and heatmaps to display findings.

## Findings

1. **Listening Activity**:
   - Total listening hours decreased as exams approached.
   - Stress periods showed more variability in genre preferences.
2. **Genre Preferences**:
   - Certain genres (e.g., instrumental or calming music) were more common during high-stress periods.
3. **Time-of-Day Trends**:
   - More listening activity was observed in the evenings during stress periods.
4. **Correlation**:
   - A negative correlation was found between days-to-exam and listening activity (-0.42, p < 0.05).

## Limitations

1. **Personalized Data**:
   - This analysis reflects my listening habits and may not generalize to others.
2. **Genre Assignment**:
   - Genre categorization was approximated based on artist names.
3. **Data Completeness**:
   - Data is limited to a single semester and may not capture long-term trends.

## Future Work

1. Analyze data across multiple semesters to observe long-term patterns.
2. Refine genre classification using Spotify's API or other metadata tools.
3. Incorporate additional metrics, such as mood or productivity data.
4. Explore advanced machine learning techniques to predict stress based on listening habits.

## How to Run the Code

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/spotify_exam_analysis.git


---

### **12. Repository Structure**
Outline the structure of your repository.

```markdown
## Repository Structure


