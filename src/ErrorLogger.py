class ErrorLogger:
  # Singleton that provides logging to a file
  instance = None

  def getInstance():
    # Our singleton "constructor"
    if ErrorLogger.instance is None :
      ErrorLogger.instance = ErrorLogger()
      ErrorLogger.instance.fileHandle = open("output.txt", 'w')
    return ErrorLogger.instance
    
  # Making the functions static... fucking python
  getInstance = staticmethod(getInstance)

  def log( self, loggingString ):
    # Logs errors to a file
    self.fileHandle.write(loggingString)

  def cleanup(self):
    print "Cleaning up"
    self.fileHandle.close()
    ErrorLogger.instance = None
