class ErrorLogger:
  # Singleton that provides logging to a file
  instance = None

  def getInstance():
    # Our singleton "constructor"
    if instance is None :
      instance = ErrorLogger()
      instance.fileHandle = open("output.txt", 'w')
    return instance
    
  # Making the functions static... fucking python
  getInstance = staticmethod(getInstance)

  def log( self, loggingString ):
    # Logs errors to a file
    file.write(loggingString)
