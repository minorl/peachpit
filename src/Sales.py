class Sales:

  LineItem = {}

  def __init__(self, dictionary):
    # Dictionary is a dictionary of whatever leslie wants it to be
    self.LineItem = dictionary

  def acceptVisitor(self, visitor):
    # visitor should be a Visitor class
    visitor.visitSales(this)
