from Parser import Parser
from Sales import Sales
import csv, sys
import datetime
import time
from datetime import *
class ExcelParser(Parser):
  # Inherited from Parser

  parsingFunctions = {}
  importRules = []
  storeNum = 0

  def importRange(self, dateRange):
    # import is a python keyword Leslie
    # dateRange is a string
    # Returns Sales class

    start = datetime.strptime(dateRange[0], "%m/%d/%y")
    end = datetime.strptime(dateRange[1], "%m/%d/%y")

    entryList=[("Number of Lines", "Date", "Reference", "G/L Account", "Description", "Amount")]

    difference = end - start
    # print difference.days
    datelist = []
    # datelist = [start - timedelta(days=x) for x in range(0, difference.days)+1]
    for i in range(0, difference.days+1):
      # datelist.append(start + timedelta(days=i))
      entryList += self.importDay('sales/'+self.storeNum +' - Daily - '+(start+timedelta(days=i)).strftime("%Y%m%d")+".CSV")
    # print datelist
    return Sales(entryList)


  def importDay(self, salesFile):
    # salesFile is a file

    entryList = []
        # File Handling ##########################################################
    #filename = '556 - Daily - 20140121.CSV'

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
