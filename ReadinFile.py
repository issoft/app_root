import xlrd
import MySQLdb

# Open the workbook and define the worksheet
book = xlrd.open_workbook("icd10cm_order_2016.xlsx") # Getsthe file and
sheet = book.sheet_by_name("icd10cm_order_2016") # Get the file name

# Establish a MySQL connection
database = MySQLdb.connect(host="localhost", user="root", passwd="issoft", db="diagnoses")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

def removePointFromCodes():
    """
    First, select  code from tb then remove '.' from the once that has it
    and update it with the value without '.'
    """
    sql = "SELECT code FROM diagnoses WHERE `type`='icd10'"
    cursor.execute(sql)
    qwery = cursor.fetchall()
    for i in qwery:
            e = ''.join(i)
            if '.' in e:
               s = e.replace('.','')
               sql = "UPDATE diagnoses SET code='%s' WHERE code='%s'" % (s, e)
               cursor.execute(sql)
            for r in range(1, sheet.nrows):
                   types='icd10'
                   Cases = sheet.cell(r, 4).value
                   sql = "SELECT code FROM diagnoses WHERE `type`='icd10'"
                   cursor.execute(sql)
                   qwery = cursor.fetchall()
                   for q in qwery:
                       t = ''.join(q)
                       sql_ = ("UPDATE diagnoses SET `case`='%s' WHERE `type`='%s' AND code='%s'" % (Cases,types, t))
                       print "passsssssss"
                   cursor.execute(sql_) # Not working yet
                   database.commit()


# add unique which code and type
# exapand the case columns
# update the server table using the temporal  table created

def readinExcelFileIntoDataBase():
    # Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
    for r in range(1, sheet.nrows):
        codes = sheet.cell(r, 1).value
        types = "icd10"
        Cases = sheet.cell(r, 4).value
        io = int(sheet.cell(r, 2).value)
        # cursor.execute("INSERT INTO TestNew (code, `type`, `Case_`, io) VALUES ('%s', '%s', '%s', '%s') ON DUPLICATE KEY UPDATE Case_='%s'" % (codes, types, Cases, io, Cases))
        cursor.execute("INSERT INTO diagnoses (`code`, `type`, `case`, `oi`) SELECT * FROM (SELECT '%s', '%s', '%s', '%s') AS tmp WHERE NOT EXISTS (SELECT code FROM diagnoses WHERE code = '%s' AND `type`='icd10')" % (codes, types, Cases, io, codes))
        database.commit()



removePointFromCodes()
# readinExcelFileIntoDataBase()
print "Success:::::::::::::"
# Close the cursor
cursor.close()

# Close the database connection
database.close()

