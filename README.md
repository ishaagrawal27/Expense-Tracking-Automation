1. Expense-Tracking-Automation

2. Project Description
This project automates the analysis of monthly financial transactions using Python.
The input transaction data is stored in a CSV file. Instead of manually calculating monthly income, expenses, balance, and transaction counts, the Python script processes the data automatically and generates a monthly summary report.

3. Objective
The objective of this project is to automate a repetitive financial data analysis task and reduce the time and effort required for manual calculations.

4. Input Data
The input file is: `monthly_transactions_january_to_june(1).csv`
The file contains transaction information including:
- Date
- Detail
- Amount
- Currency
- Debit/Credit
- Status

The sample dataset contains 90 transactions from January 2026 to June 2026.

5. Technologies Used
- Python
- Pandas
- CSV files

6. How the Script Works
i. Reads the transaction CSV file.
ii. Checks whether the required columns are available.
iii. Converts the date and amount fields into appropriate formats.
iv. Creates a month from the transaction date.
v. Separates credit and debit transactions.
vi. Calculates total monthly income.
vii. Calculates total monthly expenses.
viii. Calculates the monthly balance.
ix. Counts the number of transactions.
x. Saves the results in `monthly_summary.csv`.

7. How to Run
i) Step 1
Install Python on your computer.

 ii)Step 2
Install Pandas using: `pip install pandas`

iii) Step 3
Keep the following files in the same folder:
 - `expense_automation.py`
- `monthly_transactions_january_to_june(1).csv`

iv) Step 4
Open Command Prompt or Terminal in the project folder.

v) Step 5
Run: `python expense_automation.py`

vi) Step 6
The program will display the monthly summary and create: `monthly_summary.csv`

8. Output
The generated report contains:
- Month
- Total Income
- Total Expenses
- Balance
- Number of Transactions

9. Testing
The script was tested using a sample dataset containing 90 transactions from January 2026 to June 2026.
The dataset contains 15 transactions for each month.
The script successfully processes the transactions and generates a monthly summary automatically.

10. Conclusion
This project demonstrates how Python can automate a repetitive financial data analysis task. The automation reduces manual calculations and produces a consistent monthly report from the transaction data.
