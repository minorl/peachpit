from Factory import Factory
from ExcelParser import ExcelParser
class ExcelParserFactory(Factory):
  # Inherited from factory
  
  def createParser(self, StoreName):
    # storeName is a string
    # Returns a Parser class
    return ExcelParser()
