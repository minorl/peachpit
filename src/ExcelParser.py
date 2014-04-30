from Parser import Parser
from Sales import Sales
import csv, sys
import datetime
import time
from datetime import *
class ExcelParser(Parser):
  # Inherited from Parser

  #Things like individual handling rules should be stored
  # here, like path names per franchise, etc
  #This would be pulled from db
  parsingFunctions = {}
  importRules = []

  storeNum = ''
  refString = ''

  def __init__(self, storeName, ref):
    self.storeNum = storeName
    self.refString = ref

  def importRange(self, dateRange):
    # import is a python keyword Leslie
    # dateRange is a string

    start = datetime.strptime(dateRange[0], "%m/%d/%y")
    end = datetime.strptime(dateRange[1], "%m/%d/%y")

    #the directory as well as formatting info would be in DB
    salesDir = '../sampleData/A/'
    filePrefix = self.storeNum +' - Daily - '

    #header row for import file
    entryList=[("Number of Lines", "Date", "Reference", "G/L Account", "Description", "Amount")]

    #number of days in range
    difference = end - start

    #open and process each day in day range
    for i in range(0, difference.days+1):
      entryList += self.importDay(salesDir + filePrefix+(start+timedelta(days=i)).strftime("%Y%m%d")+".CSV")

    return Sales(entryList, self.storeNum, self.refString)


  def importDay(self, salesFile):
    # salesFile is a filename
    # Returns Sales class

    entryList = []

    number = sum(1 for row in csv.reader( open(salesFile) ) )
    with open(salesFile, 'rb') as f:
      reader = csv.reader(f, delimiter='\t')
      try :
        reader.next() #skip it
        for row in reader:
          (garbageNumber, date, line, label, account, total) = tuple(row[:6])
          entryList.append((number, date, "14WK04", account, label, total))
      except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (salesFile, reader.line_num, e))
    # End File Handling ######################################################
    return entryList

  def openFile(self, fileName):
    # filename is of type string
    # Is this really needed Leslie? Can we just do this in import day? 
    print "Function not yet implemented"
