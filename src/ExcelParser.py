from Parser import Parser
from Sales import Sales
import csv, sys
class ExcelParser(Parser):
  # Inherited from Parser

  parsingFunctions = {}
  importRules = []

  def importRange(self, dateRange):
    # import is a python keyword Leslie
    # dateRange is a string
    # Returns Sales class
    entryList = []

    # File Handling ##########################################################
    filename = '556 - Daily - 20140121.CSV'
    with open(filename, 'rb') as f:
      reader = csv.reader(f, delimiter='\t')
      try :
        for row in reader:
          (garbageNumber, date, line, label, account, total) = tuple(row[:6])
          entryList.append((number, date, "14WK04", account, label, total))
      except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
    # End File Handling ######################################################

    return Sales(entryList)

  def importDay(self, salesFile):
    # salesFile is a file
    # should this return a Sales object Leslie?
    print "Function not yet implemented"

  def openFile(self, fileName):
    # filename is of type string
    # Is this really needed Leslie? Can we just do this in import day? 
    print "Function not yet implemented"
