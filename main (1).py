from numpy import delete
import pandas as pd
from sqlalchemy import create_engine
#import vba_extract
from os import remove

FileName = 'raporti'
StartCol = 6
StartRow = 4
pd.options.display.float_format = '{:,.2f}'.format
engine = create_engine("postgresql+psycopg2://postgres:Aralytiks-2022@tp24-test.c81dvi7p7l2o.eu-central-1.rds.amazonaws.com:5432/postgres")
conn = engine.connect()
weekly_report = pd.read_sql("select * from tp_v_weekly_report", engine)
columns = list()
for column in weekly_report.keys():
    column = str(column).upper()
    column = column.replace('_', ' ')
    columns.append(column)
weekly_report.set_axis(inplace=True, axis=1, labels=columns)
writer = pd.ExcelWriter(FileName + '.xlsx', engine='xlsxwriter')
weekly_report.to_excel(writer, sheet_name='Sheet1', index=False, startcol=StartCol, startrow=StartRow)
workbook  = writer.book
workbook.add_vba_project('./vbaProject.bin')
worksheet = writer.sheets['Sheet1']
date_format = {'num_format':'mm/dd/yyyy'}
num_format = workbook.add_format({'num_format': '#,##0.00'})
percent_format = workbook.add_format({'num_format': '0.0%'})

columnWidth = 18
worksheet.set_column(1 + StartCol,1 + StartCol,50,None) #client name
worksheet.set_column(2 + StartCol,4 + StartCol,columnWidth, num_format) #loans, receiveables, eligible amount
worksheet.set_column(7 + StartCol, 9 + StartCol, columnWidth, num_format) #iniligible amount, breach, leading headroom

worksheet.set_column(5 + StartCol, 6 + StartCol, columnWidth, percent_format)# ltv, prev_ltv
worksheet.set_column(10 + StartCol, 11 + StartCol, columnWidth, percent_format) #ltv_adjusted_rate, rev_ltv_adjusted_rate

[rows, columns] = weekly_report.shape

red = workbook.add_format({'bg_color': '#ff0000'})
green = workbook.add_format({'bg_color': '#00FF00'})
yellow = workbook.add_format({'bg_color': '#FFFF00'})

# firstRow, firstColumn, lastRow, lastColumn, type....
worksheet.conditional_format(StartRow + 1, 5 + StartCol, rows + StartRow, 6 + StartCol, 
{
    'type': 'cell',
    'criteria' : '<=',
    'value' : 0.6,
    'format' : green
})

worksheet.conditional_format(StartRow + 1, 5 + StartCol, rows + StartRow, 6 + StartCol, 
{
    'type': 'cell',
    'criteria' : '<=',
    'value' : 0.7,
    'format' : yellow
})

worksheet.conditional_format(StartRow + 1, 5 + StartCol, rows + StartRow, 6 + StartCol, 
{
    'type': 'cell',
    'criteria' : '>',
    'value' : 0.7,
    'format' : red
})
# firstRow, firstColumn, lastRow, lastColumn, type....
worksheet.conditional_format(StartRow + 1, 10 + StartCol, rows + StartRow, 11 + StartCol, 
{
    'type': 'cell',
    'criteria' : '<=',
    'value' : 0.6,
    'format' : green
})

worksheet.conditional_format(StartRow + 1, 10 + StartCol, rows + StartRow, 11 + StartCol, 
{
    'type': 'cell',
    'criteria' : '<=',
    'value' : 0.7,
    'format' : yellow
})

worksheet.conditional_format(StartRow + 1, 10 + StartCol, rows + StartRow, 11 + StartCol, 
{
    'type': 'cell',
    'criteria' : '>',
    'value' : 0.7,
    'format' : red
})

workbook.filename = FileName + '.xlsm'

# ON FIRST RUN YOU HAVE TO RUN THIS, MAKE SURE U HAVE DHE MACRO SPECIFIED IN REPORT_WITH_VBA_GENERATEPDF.xlsm WITH MACRO NAME GENERATE PDF
# vba_extract.getVBA('./Report_With_VBA_GeneratePDF.xlsm')

workbook.add_vba_project('./vbaProject.bin')
# Add a button tied to a macro in the VBA project.
worksheet.insert_button('A1', {'macro':   'GeneratePDF',
                               'caption': 'Generate PDF',
                               'width':   200,
                               'height':  50})

writer.save()
del writer
remove(FileName+".xlsx")

# Open Microsoft Excel
# excel = client.Dispatch("Excel.Application")
# # Read Excel File
# sheets = excel.Workbooks.Open(os.getcwd() + '\\raporti.xlsx')
# work_sheet = sheets.Worksheets[0]
# print_area = 'A1:L'+str(rows+1)
# work_sheet.PageSetup.Zoom = False
# work_sheet.PageSetup.FitToPagesWide = 1
# work_sheet.PageSetup.LeftMargin = 25
# work_sheet.PageSetup.RightMargin = 25
# work_sheet.PageSetup.TopMargin = 50
# work_sheet.PageSetup.BottomMargin = 50
# # Convert into PDF File
# work_sheet.ExportAsFixedFormat(0, os.getcwd() + '\\raporti.pdf')
# sheets.Close(SaveChanges=0)
