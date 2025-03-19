import pandas as pd

def main():
   
    file_name = 'BusinessDS.xlsx'  

    # Read the data from the Excel file
    try:
        df = pd.read_excel(file_name, parse_dates=['Date'])
        print("Data loaded successfully.")
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # Process each row
    for index, row in df.iterrows():
        try:
            # Access the date and convert it to a string
            date_str = row['Date'].strftime('%Y-%m-%d %H:%M:%S')
            parts = date_str.split(' ')  # Split into date and time
            print(f"Row {index}: Date = {parts[0]}, Time = {parts[1]}")

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

if __name__ == "__main__":
    main()