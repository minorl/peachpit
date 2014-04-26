#!/usr/bin/python
# Testing framework
from ErrorLogger import ErrorLogger
from ExcelParser import ExcelParser
from ValidateSales import ValidateSales
from GeneratePTImport import GeneratePTImport
print "Testing..."

# Testing logger
print "Testing logger"
log = ErrorLogger.getInstance()
otherLog = ErrorLogger.getInstance()
log.log("TESTSTR")
otherLog.log("OTHER")
log.cleanup()
 
file = open("output.txt", 'r')
test = file.read()
assert "TESTSTROTHER" == test
print "Logger passed"

# Can't test to see if an object is of a Type in python so can not test
# the factory yet

print "Testing ExcelParser sales creation"
parser = ExcelParser()
sales = parser.importRange("DEBUG TEXT")
assert sales.LineItem['paul'] == 'awesome'
assert sales.LineItem['leslie'] == 'sucks'
print "Testing ExcelParser salse creation passed"

print "Testing our visitor"
visitor1 = ValidateSales()
visitor2 = GeneratePTImport()
print "Should say hello 1"
sales.acceptVisitor(visitor1)
print "should say hello 2"
sales.acceptVisitor(visitor2)
print "Testing our visitor complete"
