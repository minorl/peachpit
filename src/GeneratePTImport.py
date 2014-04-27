from Visitor import Visitor
class GeneratePTImport(Visitor):
  # Inherited from Visitor class

  def visitSales(self, sales):
    # sales is a Sales object

    # Opens file and appends it, this is bad but I am lazy
    fileHandle = open("peachpit.txt", 'a')
    for line in sales.LineItem :
      (number, date, reference, account, description, amount) = line
      # There is a cooler way to do this but fuck it
      fileHandle.write(number + "," + date + "," + reference + "," + account + \
            "," + description + "," + amount + "\n")
    fileHandle.close()
