import xlsxwriter

ventas = [
    ['Productos','Cantidad','Precio','Total'],
    ['Pack Viajes',23,699,'=B2*C2'],
    ['Vuelos',33,189,'=B3*C3'],
    ['Alojamiento',23,250,'=B4*C4'],
]
workbook = xlsxwriter.Workbook('totales.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write_row(0,0,ventas[0][0:4])
worksheet.write_row(1,0,ventas[1][0:4])
worksheet.write_row(2,0,ventas[2][0:4])
worksheet.write_row(3,0,ventas[3][0:4])

chart = workbook.add_chart({'type':'pie'})
chart.add_series({
    'categories': '=Sheet1!$A$2:$A$4',
    'values': '=Sheet1!$B$2:$B$4',
})
worksheet.insert_chart('F3',chart)
workbook.close()




