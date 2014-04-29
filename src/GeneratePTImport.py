from Visitor import Visitor
class GeneratePTImport(Visitor):
  # Inherited from Visitor class

  def visitSales(self, sales):
    # sales is a Sales object

    # Opens file and appends it, this is bad but I am lazy
    fileHandle = open("importfiles/556_14WK04.csv", 'w')
    for line in sales.LineItem :
      # print sales
      (number, date, reference, account, description, amount) = line
      # There is a cooler way to do this but fuck it
      fileHandle.write(str(number) + "," + date + "," + reference + "," + account + \
            "," + str(description) + "," + str(amount) + "\n")
    fileHandle.close()
