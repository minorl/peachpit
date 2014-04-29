#!/usr/bin/python

from ErrorLogger import ErrorLogger
from ExcelParser import ExcelParser
from ValidateSales import ValidateSales
from GeneratePTImport import GeneratePTImport
import sys

if len(sys.argv) != 5:
	print "Usage: ./peachpit.py [storenum] [refstring] [start date: mm/dd/yy] [end date: mm/dd/yy]"
	quit()

parser = ExcelParser()
parser.storeNum = str(sys.argv[2])
sales = parser.importRange((sys.argv[3], sys.argv[4]))

generateImport = GeneratePTImport()
validate = ValidateSales()
# sales.acceptVisitor(validate)
sales.acceptVisitor(generateImport)
