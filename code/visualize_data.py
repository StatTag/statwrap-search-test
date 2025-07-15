# Synthetic file created with ChatGPT

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Load dataset from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded data with shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None

def plot_histogram(df, column):
    """Plot a histogram for a given numeric column."""
    if column in df.columns:
        plt.figure(figsize=(8,6))
        sns.histplot(df[column], kde=True, bins=30, color='skyblue')
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()
    else:
        print(f"Column '{column}' not found in DataFrame.")

def plot_boxplot(df, x_col, y_col):
    """Plot a boxplot for category vs numeric variable."""
    if x_col in df.columns and y_col in df.columns:
        plt.figure(figsize=(10,6))
        sns.boxplot(x=df[x_col], y=df[y_col], palette='pastel')
        plt.title(f'Boxplot of {y_col} by {x_col}')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.show()
    else:
        print(f"Columns '{x_col}' and/or '{y_col}' not found in DataFrame.")

def plot_correlation_heatmap(df):
    """Plot a correlation heatmap for numerical features."""
    plt.figure(figsize=(10,8))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", square=True)
    plt.title('Correlation Heatmap')
    plt.show()

def main():
    file_path = "final-dataset.csv"
    df = load_data(file_path)
    if df is not None:
        # Example plots assuming these columns exist
        plot_histogram(df, 'value')
        plot_boxplot(df, 'category', 'value')
        plot_correlation_heatmap(df)

if __name__ == "__main__":
    main()
