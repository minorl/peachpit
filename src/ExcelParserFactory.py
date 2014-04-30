from Factory import Factory
from ExcelParser import ExcelParser
class ExcelParserFactory(Factory):
  # Inherited from factory
  
  def createParser(self, StoreName, ref):
    # storeName is a string
    # Returns a Parser class
    return ExcelParser(StoreName, ref)
