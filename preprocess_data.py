import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process an Excel file.')
    parser.add_argument('--file_path', type=str, default='BusinessDS.xlsx', help='Path to the Excel file')
    args = parser.parse_args()

    # Read the data from the Excel file
    try:
        df = pd.read_excel(args.file_path, parse_dates=['Date'])
        print("Data loaded successfully.")
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # Report general statistics
    print("\n=== General Statistics ===")
    num_samples = df.shape[0]  # Number of rows (samples)
    num_features = df.shape[1]  # Number of columns (features)
    print(f"Number of samples (rows): {num_samples}")
    print(f"Number of features (columns): {num_features}")
    print("\nDataset Info:")
    print(df.info())
    print("\nDescriptive Statistics:")
    print(df.describe(include='all'))

    # Process each row
    for index, row in df.iterrows():
        try:
            # Access the date and convert it to a string
            date_str = row['Date'].strftime('%Y-%m-%d %H:%M:%S')
            parts = date_str.split(' ')  # Split into date and time
            print(f"\nRow {index}: Date = {parts[0]}, Time = {parts[1]}")

            # Access other columns
            file_name = row['File Name']
            position_type = row['Position Type']
            ticker = row['Ticker']
            ratio = row['Ratio']
            current_price = row['Current Price']
            reference_price = row['Reference Price']
            average = row['Average']

            # Print or process the data
            print(f"File: {file_name}, Ticker: {ticker}, Position: {position_type}")
            print(f"Ratio: {ratio}, Current Price: {current_price}, Reference Price: {reference_price}, Average: {average}")
            print("-" * 40)
        except KeyError as e:
            print(f"Missing column in row {index}: {e}")
        except Exception as e:
            print(f"Error parsing row {index}: {e}")

    print("Processing complete.")

    # Save the processed data to a new CSV file
    output_csv_path = 'processed_data.csv'
    df.to_csv(output_csv_path, index=False)
    print(f"\nProcessed data saved to {output_csv_path}")

    # Save to a new Excel file
    output_excel_path = 'processed_data.xlsx'
    df.to_excel(output_excel_path, index=False)
    print(f"Processed data saved to {output_excel_path}")

    # Calculate business statistics
    print("\n=== Business Statistics ===")
    print("Basic Statistics:")
    print(df.describe())

    # Filter rows where Position Type is 'L' (Long)
    long_positions = df[df['Position Type'] == 'L']
    print("\nLong Positions:")
    print(long_positions)

    # Group by Ticker and calculate the average ratio
    grouped_data = df.groupby('Ticker')['Ratio'].mean()
    print("\nAverage Ratio by Ticker:")
    print(grouped_data)

    # Plot the distribution of the 'Ratio' column
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Ratio'], bins=20, kde=True)
    plt.title('Distribution of Ratios')
    plt.xlabel('Ratio')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == "__main__":
    main()