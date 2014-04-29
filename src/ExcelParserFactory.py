from Factory import Factory
class ExcelParserFactory(Factory):
  # Inherited from factory
  
  def createParser(self, StoreName):
    # storeName is a string
    # Returns a Parser class
    return ExcelParser()
