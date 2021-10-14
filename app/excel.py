import openpyxl
from openpyxl.styles import Alignment
from openpyxl.utils import get_column_letter

path = "test.xlsx"
wb = openpyxl.Workbook()
sheet_name = wb.sheetnames
sheet = wb[sheet_name[0]]


def centralize_text():
    for cellObj in sheet['A1':'D2']:
        for cell in cellObj:
            cell.alignment = Alignment(horizontal='center')


def fill_file(data):
    i = 1
    for d in data:
        print(d)
        sheet.cell(row=1, column=i).value = d
        sheet.cell(row=2, column=i).value = data[d]
        i+=1


def optimize_columns_width():
    for i in range(1, 8):
        cell = sheet.cell(row=2, column=i)
        sheet.column_dimensions[get_column_letter(cell.column)] \
            .width = max(len(str(cell.value)), len(str(sheet[f'{get_column_letter(i)}1'].value))) + 6


def form_file(data):
    fill_file(data)
    optimize_columns_width()
    centralize_text()
    wb.save(path)
