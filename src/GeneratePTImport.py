from Visitor import Visitor
class GeneratePTImport(Visitor):
  # Inherited from Visitor class

  def visitSales(self, sales):
    # sales is a Sales object
    for line in sales.LineItem :
      (number, date, reference, account, description, amount) = line
      # There is a cooler way to do this but fuck it
      print number + "," + date + "," + reference + "," + account + \
            "," + description + "," + amount
