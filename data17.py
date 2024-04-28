from openpyxl import load_woorkbook
wb = load_workbook("테스트.xlsx")
wb.copy_worksheet(wb["시트1"])
wb.active = wb["시트1 Copy"]
wb.save(filename = "샘플_시트 복사.xlsx")