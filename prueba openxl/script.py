import openpyxl


	
doc= openpyxl.load_workbook("prueba.xlsx")
hoja= doc.get_sheet_by_name('hoja')
hoja['B2'] = "HECHO"

hoja.cell(row=4, column=2, value="hola")	
doc.save("prueba.xlsx")
cadena ="hola3ms con 45 en linea"
b= int(cadena)
print


