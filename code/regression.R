# regression.R - Synthetic file created with ChatGPT

# Load necessary libraries
library(readr)
library(dplyr)

# Load the data
data <- read_csv("../data/processed/final-dataset.csv")

# Quick look at the data
print("First few rows of the data:")
print(head(data))

# Do a simple linear regression: value ~ score
model <- lm(value ~ score, data = data)

# Print the summary of the model
print("Summary of the linear regression model:")
print(summary(model))

# Optional: plot the regression
plot(data$score, data$value, 
     main = "Linear Regression of Value vs Score",
     xlab = "Score", ylab = "Value", pch = 19, col = "blue")
abline(model, col = "red", lwd = 2)
