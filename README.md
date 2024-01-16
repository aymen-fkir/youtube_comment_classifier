# Project Overview

## Toxic Comment Classification and Analysis

### Introduction:
This project involves analyzing and classifying comments from Youtube comment section to identify toxic content. The goal is to create a comprehensive system that can process comments, classify them based on toxicity, and generate insightful visualizations to understand the distribution of toxic scores.

### Components:

1. **Toxic Comment Classification:**
    - Utilizes the Hugging Face API to classify comments into toxic and non-toxic categories.
    - The `classify_comment` function takes a comment as input, sends it to the Hugging Face API, and retrieves the classification results.

2. **Comment Organization:**
    - The `organise_comments` function processes a list of comments, classifies each comment using the Hugging Face API, and creates a DataFrame with columns for comment text, label, and toxicity score.
    - The results are saved to a CSV file named "comments.csv" for further analysis.

3. **YouTube Comment Retrieval:**
    - The `Get_comments` function utilizes the YouTube API to fetch comments from a specified video.
    - The retrieved comments are preprocessed to handle emojis and stored in a DataFrame before being saved to "comments.csv."

4. **Toxicity Analysis with OpenAI:**
    - The `get_conclusion` function uses the SmartDataframe library and OpenAI's language model to generate a chart based on non-toxic comments.
    - The chart visualizes the toxicity scores of comments, with the x-axis representing the index column and the y-axis representing the toxicity score.

### Usage:

- **Requirements:**
  - Ensure that you have the required API keys and environment variables set up (Hugging Face API key, OpenAI API key, and YouTube API key).

- **Execution:**
  - Execute the scripts in the following order:
    1. `get_comments.py`: Fetches comments from a specified YouTube video.
    2. `classify.py`: Classifies comments using the Hugging Face API and organizes the data into a DataFrame.
    3. `conclude.py`: Utilizes OpenAI and SmartDataframe to generate a toxicity score chart for non-toxic comments.

### Notes:
- The generated "comments.csv" file serves as the central dataset for comment analysis.
- Ensure that all necessary Python libraries are installed before running the scripts (`pandas`, `requests`, `googleapiclient`, `pandasai`, etc.).

Feel free to customize and extend the project according to your specific requirements.
