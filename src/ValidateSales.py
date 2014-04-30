from Visitor import Visitor
class ValidateSales(Visitor):
  # Inherits from Visitor

  def visitSales(self, sales):
    # sales is a Sales object
    #should check to make sure total is zero, 
    #over short isn't outrageous
    print "hello 1"
