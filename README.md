# Financial Dataset Preprocessing and Analysis

This project focuses on preprocessing and analyzing a financial dataset containing information about stock positions, including dates, file names, position types, tickers, ratios, current prices, reference prices, and averages. The dataset is stored in an Excel file, and the analysis is conducted using Python.

## **Features**
- **General Statistics**: Report the number of samples (rows) and features (columns) in the dataset, along with descriptive statistics.
- **Categorical and Continuous Features**: Identify and visualize the distribution of categorical and continuous features.
- **Outlier Detection**: Detect outliers using two methods: Z-Score and Interquartile Range (IQR).
- **Missing Values**: Report statistics on missing values and treat them appropriately.
- **Data Cleaning Actions**: Suggest probable data cleaning actions based on the analysis.
- **Normalization**: Normalize the dataset and save the normalized data for further use.
- **Feature Relationships**: Visualize important relationships between features to gain insights into the dataset.

## **Requirements**
To run this project, you need the following Python libraries:
- `pandas`
- `matplotlib`
- `seaborn`
- `scipy`
- `scikit-learn`
- `openpyxl`

You can install the required libraries using the following command:
```bash
pip install pandas matplotlib seaborn scipy scikit-learn openpyxl
