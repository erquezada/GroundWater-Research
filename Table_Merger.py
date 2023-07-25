import pandas as pd

def merge_excel_files(file1, file2, sheet1, sheet2, output_file):
    # Read the Excel file
    excel_file1 = pd.ExcelFile(file1)
    excel_file2 = pd.ExcelFile(file2)

    # Read the specified sheets from the Excel file
    df1 = excel_file1.parse(sheet1)
    df2 = excel_file2.parse(sheet2)

    # Merge the dataframes based on the 'Well Number' column
    merged_df = pd.merge(df1, df2, on='WI Unique Well No', how='inner')

    # Save the merged dataframe to a new Excel file
    merged_df.to_excel(output_file, index=False)
    print(f"Merged data saved to {output_file}")

# Example usage
file1 = 'Updated_Radium_Data.xlsx'
file2 = 'Sand and Gravel filtered DNR.xlsx'
sheet1 = 'Radium'
sheet2 = 'Sheet1'
output_file = 'All Wells Ra DNR Merged version 2.xlsx'

merge_excel_files(file1,file2, sheet1, sheet2, output_file)
