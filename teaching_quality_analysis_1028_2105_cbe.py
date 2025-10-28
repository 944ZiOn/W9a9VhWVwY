# 代码生成时间: 2025-10-28 21:05:36
import numpy as np

"""
Teaching Quality Analysis Program

This program analyzes teaching quality using numpy. It calculates various statistics
such as mean, median, and standard deviation of scores to provide insights.
"""

# Define constants for score data
SCORE_DATA = np.array([
    [90, 85, 95, 90],
    [75, 80, 85, 80],
    [95, 90, 85, 95],
    [80, 75, 80, 75]
])

# Function to calculate mean score
def calculate_mean(scores):
    """Calculate the mean score."""
    return np.mean(scores)

# Function to calculate median score
def calculate_median(scores):
    """Calculate the median score."""
    return np.median(scores)

# Function to calculate standard deviation
def calculate_std_dev(scores):
    """Calculate the standard deviation of scores."""
    return np.std(scores)

# Main function to analyze teaching quality
def analyze_teaching_quality():
    """Analyze teaching quality and print statistics."""
    try:
        # Calculate and print statistics
        mean_score = calculate_mean(SCORE_DATA)
        median_score = calculate_median(SCORE_DATA)
        std_dev = calculate_std_dev(SCORE_DATA)

        print(f"Mean Score: {mean_score}")
        print(f"Median Score: {median_score}")
        print(f"Standard Deviation: {std_dev}")

    except Exception as e:
        # Handle any exceptions that occur during analysis
        print(f"Error occurred: {str(e)}")

# Entry point of the program
if __name__ == "__main__":
    analyze_teaching_quality()