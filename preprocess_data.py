# Step 1: Import the required libraries
import pandas as pd

# Step 2: Define the data as a list of strings
data = [
    "Nov 27 2012_006 Big_100_1_LONG_SHORT_F.pdf, L, GOOG 1.053 =695.00/660.17, Avg of 1 = 1.053",
    "Nov 27 2012_006 Big_100_1_LONG_SHORT_F.pdf, S, AAPL 0.987 =581.80/589.55, Avg of 1 = 0.987",
    "Nov 27 2012_006 Big_100_2_LONG_SHORT_F.pdf, L, DIS 1.004 =49.25/49.06, GOOG 1.053 =695.00/660.17, Avg of 2 = 1.028",
    "Nov 27 2012_006 Big_100_2_LONG_SHORT_F.pdf, S, AAPL 0.987 =581.80/589.55, FB 1.039 =27.06/26.04, Avg of 2 = 1.013",
    # Add more rows here if needed
]

# Step 3: Create a function to parse each row
def parse_row(row):
    # Split the row by commas
    parts = row.split(", ")
    
    # Extract the date and file name
    date_file = parts[0].split("_")
    date = " ".join(date_file[:3])  # Extract the date (e.g., "Nov 27 2012")
    file_name = "_".join(date_file[3:])  # Extract the file name
    
    # Extract the position type (L or S)
    position_type = parts[1]
    
    # Extract the ticker, ratio, and prices
    ticker_data = parts[2].split(" ")
    ticker = ticker_data[0]  # Extract the ticker (e.g., "GOOG")
    ratio = float(ticker_data[1])  # Extract the ratio (e.g., 1.053)
    prices = ticker_data[3].split("/")
    current_price = float(prices[0])  # Extract the current price (e.g., 695.00)
    reference_price = float(prices[1])  # Extract the reference price (e.g., 660.17)
    
    # Extract the average
    average = float(parts[-1].split(" = ")[1])  # Extract the average (e.g., 1.053)
    
    # Return the parsed data as a dictionary
    return {
        "Date": date,
        "File Name": file_name,
        "Position Type": position_type,
        "Ticker": ticker,
        "Ratio": ratio,
        "Current Price": current_price,
        "Reference Price": reference_price,
        "Average": average,
    }

# Step 4: Parse all rows and store them in a list
parsed_data = [parse_row(row) for row in data]

# Step 5: Convert the list of dictionaries into a Pandas DataFrame
df = pd.DataFrame(parsed_data)

# Step 6: Save the DataFrame to a CSV file
df.to_csv("processed_data.csv", index=False)

# Step 7: Print the DataFrame to verify
print(df)

