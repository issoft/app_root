import xlrd
import MySQLdb

# Open the workbook and define the worksheet
# book = xlrd.open_workbook("icd10cm_order_2016.xlsx") # Getsthe file and
# sheet = book.sheet_by_name("icd10cm_order_2016") # Get the file name

ob = open("diagnoses_full.sql", 'r')


# Establish a MySQL connection
database = MySQLdb.connect(host="localhost", user="root", passwd="issoft", db="diagnoses")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# sql that create table
# CREATE TABLE `diagnoses_full` (
#   `id` int(11) NOT NULL,
#   `code` varchar(10) DEFAULT NULL,
#   `type` enum('icd10','icpc-2') NOT NULL DEFAULT 'icd10',
#   `case` varchar(500) DEFAULT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=latin1;


#
# def alter():
#     UPDATE `diagnoses_copy` set code = replace(code, ".","");
#     ALTER TABLE `diagnoses_copy` ADD UNIQUE( `code`, `type`);
#     ALTER TABLE `diagnoses_copy` CHANGE `case` `case` VARCHAR(500) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL;
#    ALTER TABLE `diagnoses_copy` CHANGE `oi` `oi` BOOLEAN NOT NULL DEFAULT TRUE;
#
# cursor.execute("INSERT INTO `diagnoses` (`code`, `type`, `case`) SELECT `code`,`type`, `case` FROM '%s' ON DUPLICATE KEY UPDATE `code` = VALUES(`code`), `type` = VALUES(`type`), `case` = VALUES(`case`)" %(ob))
# database.commit()
#
# ob.close()
# cursor.close()
# database.close()