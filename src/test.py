# Testing framework
from ErrorLogger import ErrorLogger
print "Testing..."

# Testing logger
print "Testing logger"
log = ErrorLogger()
log.log("TESTSTR")
file = open("output.txt", 'r')
test = file.read()
print test
assert "TESTSTR" == test
print "Logger passed"
