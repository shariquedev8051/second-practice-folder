

# 1. Excel file handling cheat sheet

- [1. Excel file handling cheat sheet](#1-excel-file-handling-cheat-sheet)
    - [1.0.1. **Writting data in sheet:-**](#101-writting-data-in-sheet-)
    - [1.0.2. **Saving sheet to the excel file:**](#102-saving-sheet-to-the-excel-file)
    - [1.0.3. **Try catch for risky code**](#103-try-catch-for-risky-code)
    - [1.0.4. **For reading data from excel sheet**](#104-for-reading-data-from-excel-sheet)
  
Import modules

```python
import openpyxl as xcl

```
------------------
### 1.0.1. **Writting data in sheet:-**
Create a workbook i.e excel file

```python
wb =  openpyxl.workbook()
```

Create sheet to store data in it
```python
sheet = wb.active
```

1. First methode
```python
sheet["A1"] = 'ABC'
```
2. Second methode
```python
sheet.cell(row, column).value = 'abc'
```

### 1.0.2. **Saving sheet to the excel file:**
1. select the path
```python
FILE_PATH = r"f:\This \is \the \file \path \with \r" 

FILE_PATH = "f:\\This \\is \\escape \\ characters\\ sequence."
```
2. save sheet using command

```python
wb.save(FILE_PATH)
```
---------
### 1.0.3. **Try catch for risky code**
```python
try:
    wb.save(FILE_PATH)
except PermissionError:
    print('Pleas close the file!!')
```

------
### 1.0.4. **For reading data from excel sheet**
```python
FILE_PATH = 'From where you want to read data'
```
Loading workbook
```python
wb = xcl.load_workbook(FILE_PATH)
```
Activating sheet
```python
sheet = wb.active
```
Reading cell value
```python
print(sheet.cell(row,column).value)
```