from Visitor import Visitor
class GeneratePTImport(Visitor):
  # Inherited from Visitor class

  def visitSales(self, sales):
    # sales is a Sales object
    #create file name string

    #this would be stored in db
    completedDir = "../importfiles/"
    fileName = sales.storeNum + "_" + sales.ref + ".csv"

    # Opens file and appends it, this is bad but I am lazy
    fileHandle = open(completedDir + fileName, 'w')
    for line in sales.LineItem :

      (number, date, reference, account, description, amount) = line
      # There is a cooler way to do this but f&%! it [paul don't swear in comments, dana reads them all]
      fileHandle.write(str(number) + "," + date + "," + reference + "," + account + \
            "," + str(description) + "," + str(amount) + "\n")
    fileHandle.close()
