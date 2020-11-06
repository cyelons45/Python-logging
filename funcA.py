import logging
from loggerTool import Logger
Logger = Logger()


class AddandMultiply(object):
    """
    Class to perform additions and multiplications
    Attributes:
    object(object): Inheriting from the parent object.
    """

    def __init__(self, *args):
        """This is a constructor to set user input."""
        self.values = args
        # self. Logger = Logger()

    def add(self):
        """Method to add input values"""
        try:
            val = 0
            for num in self.values:
                val = val + num
            Logger.printInfoMessage("Values added successfully")
            return val
        except Exception as e:
            Logger.printErrorMessage("Addition failed")

    def multiply(self):
        """Method to multiply input values"""
        try:
            val = 1
            for num in self.values:
                val = val * num
            Logger.printInfoMessage("Values were multiplied successfully")
            return val
        except Exception as e:
            Logger.printErrorMessage('Multiplication failed')


if __name__ == "__main__":
    pass
