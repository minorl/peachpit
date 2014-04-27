from Parser import Parser
from Sales import Sales
class ExcelParser(Parser):
  # Inherited from Parser

  parsingFunctions = {}
  importRules = []

  def importRange(self, dateRange):
    # import is a python keyword Leslie
    # dateRange is a string
    # Returns Sales class
    entryList = [("10", "1/20/2014", "14WK04", "41000", "Food", "-741.63")] 
    return Sales(entryList)

  def importDay(self, salesFile):
    # salesFile is a file
    # should this return a Sales object Leslie?
    print "Function not yet implemented"

  def openFile(self, fileName):
    # filename is of type string
    # Is this really needed Leslie? Can we just do this in import day? 
    print "Function not yet implemented"
