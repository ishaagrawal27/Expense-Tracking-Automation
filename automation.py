import pandas as pd
import os

# --------------------------------------------------
# 1. File names
# --------------------------------------------------

input_file = "monthly_transactions_january_to_june(1).csv"
output_file = "monthly_summary.csv"


# --------------------------------------------------
# 2. Check whether the input file exists
# --------------------------------------------------

if not os.path.exists(input_file):
    print("Error: Transaction file was not found.")
    print("Make sure the CSV file is in the same folder as this Python file.")
    exit()


# --------------------------------------------------
# 3. Read the transaction data
# --------------------------------------------------

try:
    data = pd.read_csv(input_file)
except Exception as e:
    print("Error while reading the CSV file:", e)
    exit()


# --------------------------------------------------
# 4. Check required columns
# --------------------------------------------------

required_columns = [
    "Date",
    "Detail",
    "Amount",
    "Currency",
    "Debit/Credit",
    "Status"
]

missing_columns = [
    column for column in required_columns
    if column not in data.columns
]

if missing_columns:
    print("Error: Missing columns:", missing_columns)
    exit()


# --------------------------------------------------
# 5. Convert Date column into proper date format
# --------------------------------------------------

data["Date"] = pd.to_datetime(data["Date"], errors="coerce")

if data["Date"].isna().any():
    print("Warning: Some dates could not be converted.")


# --------------------------------------------------
# 6. Make sure Amount contains numbers
# --------------------------------------------------

data["Amount"] = pd.to_numeric(data["Amount"], errors="coerce")

if data["Amount"].isna().any():
    print("Warning: Some transaction amounts are invalid.")


# --------------------------------------------------
# 7. Create a Month column
# --------------------------------------------------

data["Month"] = data["Date"].dt.strftime("%Y-%m")


# --------------------------------------------------
# 8. Calculate monthly income and expenses
# --------------------------------------------------

monthly_income = (
    data[data["Debit/Credit"].str.lower() == "credit"]
    .groupby("Month")["Amount"]
    .sum()
)

monthly_expenses = (
    data[data["Debit/Credit"].str.lower() == "debit"]
    .groupby("Month")["Amount"]
    .sum()
)

transaction_count = (
    data.groupby("Month")
    .size()
)


# --------------------------------------------------
# 9. Create the monthly summary
# --------------------------------------------------

months = sorted(data["Month"].dropna().unique())

summary = pd.DataFrame({
    "Month": months
})

summary["Total Income"] = (
    summary["Month"]
    .map(monthly_income)
    .fillna(0)
)

summary["Total Expenses"] = (
    summary["Month"]
    .map(monthly_expenses)
    .fillna(0)
)

summary["Balance"] = (
    summary["Total Income"] -
    summary["Total Expenses"]
)

summary["Number of Transactions"] = (
    summary["Month"]
    .map(transaction_count)
    .fillna(0)
    .astype(int)
)


# --------------------------------------------------
# 10. Save the automated report
# --------------------------------------------------

summary.to_csv(output_file, index=False)


# --------------------------------------------------
# 11. Display the result
# --------------------------------------------------

print("\n==============================================")
print("       MONTHLY TRANSACTION SUMMARY")
print("==============================================\n")

print(summary.to_string(index=False))

print("\n==============================================")
print("Report generated successfully!")
print("Output file:", output_file)
print("==============================================")
