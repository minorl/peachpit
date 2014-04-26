from Visitor import Visitor
class GeneratePTImport(Visitor):
  # Inherited from Visitor class

  def visitSales(self, sales):
    # sales is a Sales object
    print "hello 2"
