
import openpyxl as xcl
import os
os.system('cls')
from GenrateEmpDataDict import GenrateEmpData


def main():
    print(GenrateEmpData(110,1))
    FILE_PATH = r'E:\Videos softech\70-73 Excel File Handling\Excel_fiel_handling.xlsx'
    wb = xcl.Workbook()
    sheet = wb.active

if __name__ == '__main__':
    main()