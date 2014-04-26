# Testing framework
from ErrorLogger import ErrorLogger
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
