import pandas as pd

# CSV file ka naam yahan likho
csv_file = 'books_data.csv'

# Excel file ka naam yahan likho
excel_file = 'output_data.xlsx'

# CSV file read karo
data = pd.read_csv(csv_file)

# Excel file me save karo
data.to_excel(excel_file, index=False)

print("Conversion Successful! ")
