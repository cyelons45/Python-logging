import logging
from loggerTool import Logger
Logger = Logger()


class SubtractandDivide(object):
    """
    Class to perform subtraction and divisions.
    Attributes:
    object(object): Inheriting from the parent object.
    """

    def subtract(self, a, b):
        """Method to subtract input values"""
        try:
            Logger.printInfoMessage("Values subtracted successfully")
            return a - b
        except Exception as e:
            Logger.printErrorMessage("Subtraction failed" + str(e))

    def divide(self, a, b):
        """Method to divide input values"""
        try:
            Logger.printInfoMessage("Values divided successfully")
            return a/b
        except Exception as e:
            Logger.printErrorMessage("Division failed"+str(e))


if __name__ == "__main__":
    pass
