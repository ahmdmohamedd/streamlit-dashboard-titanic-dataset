# Streamlit Dashboard - Titanic Dataset

An interactive dashboard built with Streamlit to explore the Titanic dataset. This project allows users to visualize key insights from the dataset through various interactive charts and graphs.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Visualizations](#visualizations)
- [How to Run](#how-to-run)
- [Results](#results)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Introduction
The Titanic dataset contains data about passengers who were aboard the Titanic, including their demographics and whether they survived the tragedy. This dashboard presents an interactive way to analyze and visualize this dataset.

## Features
- **Passenger Class Distribution**: Visualizes the number of passengers across different classes.
- **Survival Rate by Gender**: Displays the survival rates based on gender.
- **Age Distribution**: Shows the distribution of passengers' ages.

## Installation
To run this project, you need to have Python and the necessary libraries installed. You can create a new conda environment and install the required packages using the following commands:

```bash
conda create -n streamlit-dashboard python=3.8
conda activate streamlit-dashboard
conda install -y streamlit pandas matplotlib seaborn
```

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/ahmdmohamedd/streamlit-dashboard-titanic-dataset.git
   cd streamlit-dashboard-titanic-dataset
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run titanic_dashboard.py
   ```

3. Open your web browser and navigate to `http://localhost:8501` to view the dashboard.

## Visualizations
The dashboard includes the following visualizations:
- **Passenger Class Distribution**: A bar chart showing the distribution of passengers in different classes.
- **Survival Rate by Gender**: A bar chart representing the survival rates of male and female passengers.
- **Age Distribution**: A histogram displaying the age distribution of passengers.

## How to Run
To run the Streamlit application:
1. Open your terminal or Anaconda Prompt.
2. Navigate to the project directory.
3. Use the command to run the Streamlit application as shown in the **Usage** section.

## Results
The PDF version of the dashboard (`titanic_dashboard.pdf`) is also included in the repository for easy viewing and sharing.

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## Acknowledgments
- The Titanic dataset is sourced from [Kaggle](https://www.kaggle.com/c/titanic).
- This project utilizes the Streamlit library for building the dashboard and visualizing data.
