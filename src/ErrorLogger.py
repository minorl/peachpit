class ErrorLogger:

  def log( self, loggingString ):
    # Logs errors to a file
    file = open("output.txt", 'w')
    file.write(loggingString)
    file.close
