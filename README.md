# Anime Recommender System

## Project Overview

### 1.1 Introduction

Anime has become a global phenomenon, captivating audiences with its diverse genres and storytelling. With an ever-growing catalog, discovering new anime that aligns with personal preferences can be challenging. This project presents an **Anime Recommender System** that analyzes user preferences to suggest anime titles tailored to individual tastes.

### 1.2 Problem Statement

Selecting the next anime to watch is often overwhelming due to the vast number of available titles and genres. Traditional search methods may not effectively surface anime that align with a user's unique preferences. This project employs data-driven techniques to identify and recommend anime that users are likely to enjoy, enhancing their viewing experience.

### 1.3 Aim

The primary aim is to develop a recommendation system that provides personalized anime suggestions by analyzing user preferences and anime attributes. By leveraging collaborative filtering and content-based filtering methods, the system delivers accurate and relevant recommendations.

### 1.4 Objectives

- **Data Analysis**: Perform a comprehensive analysis of anime datasets to understand trends and user preferences.
- **Model Development**: Implement collaborative and content-based filtering algorithms to generate recommendations.
- **Evaluation**: Assess the performance of the recommendation models using appropriate metrics.
- **User Interface**: Develop an interactive web application for users to receive personalized anime recommendations.

## 2. Importing Packages

The project utilizes various Python libraries for data manipulation, visualization, and machine learning:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
import warnings
warnings.filterwarnings('ignore')
```

## 3. Loading Data

The dataset, `anime.csv`, is loaded into the workspace using pandas for analysis.

```python
# Load the dataset
anime_df = pd.read_csv("anime.csv")
print(anime_df.head())
```

## 4. Data Cleaning

Data cleaning ensures the dataset is suitable for analysis. The steps include:

- **Handling Missing Values**: Fill or remove missing values in relevant columns.
- **Renaming Columns**: Rename columns for clarity.
- **Handling Duplicates**: Check and handle duplicate rows.

```python
# Fill missing values
anime_df['genre'].fillna('Unknown', inplace=True)

# Rename columns for clarity
anime_df.rename(columns={'name': 'Title', 'genre': 'Genre', 'rating': 'Rating'}, inplace=True)

# Check for duplicates
duplicate_values = anime_df.duplicated().sum()
```

## 5. Exploratory Data Analysis (EDA)

EDA helps visualize key trends and patterns in the data, providing insights into relationships between variables such as:

- **Genre Distribution**: Analyze the distribution of anime genres.
- **Rating Analysis**: Examine the distribution of anime ratings.

```python
# Visualize genre distribution
plt.figure(figsize=(10,6))
sns.countplot(y=anime_df['Genre'], order=anime_df['Genre'].value_counts().index)
plt.title("Distribution of Anime Genres")
plt.show()
```

## 6. Machine Learning Model

The system employs collaborative filtering to predict user preferences based on historical data. The workflow includes:

- **Data Preprocessing**: Encode categorical variables and scale numerical features.
- **Model Training**: Train the model using the cleaned dataset.
- **Evaluation**: Assess the model's performance using metrics like accuracy and F1-score.

```python
# Example of model training
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Assuming 'features' and 'target' are predefined
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predictions and evaluation
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
f1 = f1_score(y_test, predictions, average='weighted')
```

## 7. Interactive Visualizations and Predictions

The project includes an interactive web app built with Streamlit, allowing users to:

- **Explore Visualizations**:
  - **Genre Distribution**: View the distribution of anime genres.
  - **Rating Analysis**: Examine the distribution of anime ratings.

- **Make Predictions**:
  - Input anime preferences to receive personalized recommendations.

```python
# Streamlit app example
import streamlit as st

st.title("Anime Recommender System")

# User input
user_genre = st.selectbox("Select Genre", anime_df['Genre'].unique())
user_rating = st.slider("Select Minimum Rating", 0, 10, 5)

# Filtered recommendations
recommendations = anime_df[(anime_df['Genre'] == user_genre) & (anime_df['Rating'] >= user_rating)]
st.write("Recommended Anime Titles:", recommendations['Title'].tolist())
```

## Conclusion

This project demonstrates how data analysis and machine learning can provide insights and predictions in the anime domain. The interactive app enhances user engagement, making it easy for anime enthusiasts to discover new titles aligned with their preferences.

---
