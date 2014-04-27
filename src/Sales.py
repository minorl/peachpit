class Sales:

  LineItem = []

  def __init__(self, entryList):
    # entryList is a list of a peachpit line entry, it is a tuple like this
    # (Number, Date, Reference, Account, Descriptions, Amount)
    # Each element of this tuple should be a string
    self.LineItem = entryList 

  def acceptVisitor(self, visitor):
    # visitor should be a Visitor class
    visitor.visitSales(self)
