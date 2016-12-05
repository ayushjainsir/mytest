import xlrd
import MySQLdb
book = xlrd.open_workbook("myxlsheet.xls")
sheet = book.sheet_by_index(0)
database = MySQLdb.connect (host="localhost", user = "root", passwd = "root", db = "dblock")
cursor = database.cursor()
query = """INSERT INTO mytb (name, roomno, year) VALUES (%s, %s, %s )"""

for r in range(1, sheet.nrows):
    roomno = sheet.cell(r,1).value
    name = sheet.cell(r,2).value
    year = sheet.cell(r,5).value
    value = (name, roomno, year)
    cursor.execute(query, value)
cursor.close()
database.commit()
database.close()
	
