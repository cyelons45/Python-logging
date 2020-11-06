import logging
import os
import datetime


class Logger:
    """Support class for creating logs"""

    def __init__(self):
        """
        Constructor: This takes no attributes. Everything is hard coded.
        """
        try:
            # Create path for log files
            loggerPath = 'C:/UC2020/Logs/'
            loggerName = 'GM GT GPOM_DELTA'

            # Create time for logs
            self.now = datetime.datetime.now()

            # Create directory for logs if not exist
            if not os.path.exists(loggerPath):
                os.makedirs("C:/UC2020/Logs/")

            # Create log file name
            loggerFileName = loggerName + \
                self.now.strftime(' %Y-%m-%d %H-%M')+'.log'

            # create logger with 'loggerFileName'
            logger = logging.getLogger(loggerFileName)
            logger.setLevel(logging.DEBUG)

            # create file handler which logs even debug messages
            fh = logging.FileHandler(loggerPath + loggerFileName, mode='w')
            fh.setLevel(logging.DEBUG)

            # create console handler with a higher log level
            ch = logging.StreamHandler()
            ch.setLevel(logging.ERROR)

            # create formatter and add it to the handlers
            formatter = logging.Formatter(
                '%(asctime)s :   %(message)s  ', datefmt='%Y/%m/%d %H:%M:%S')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # add the handlers to the logger
            logger.addHandler(fh)
            logger.addHandler(ch)

            self.logger = logger
            self.loggerPath = loggerPath
            self.loggerFileName = loggerFileName

        except Exception as e:
            print("Logger failed to initialize " + str(e))

    def printInfoMessage(self, message):
        """
        Function to print message to log fileself.
        Args:
        message(string):message to be printedself.
        Returns: None
        """
        try:
            message = self.logger.info(str(message) + " " +
                                       self.now.strftime(' %Y-%m-%d %H-%M'))
            print(message)
        except Exception as e:
            print('Logger failed in printInfoMessage')
            self.logger.error('Logger failed in printInfoMessage' + " " +
                              self.now.strftime(' %Y-%m-%d %H-%M'))

    def printErrorMessage(self, message):
        """
        Function to print message to log fileself.
        Args:
        message(string):message to be printedself.
        Returns: None
        """
        try:
            message = self.logger.error(str(message) + " " +
                                        self.now.strftime(' %Y-%m-%d %H-%M'))
            print(message)
            self.logger.error(message + " " +
                              self.now.strftime(' %Y-%m-%d %H-%M'))
        except Exception as e:
            print('Logger failed in printErrorMessage')
            self.logger.error('Logger failed in printErrorMessage' + " " +
                              self.now.strftime(' %Y-%m-%d %H-%M'))

    def getLoggerPathAndFilename(self):
        """
        Function to return logger path and filename.
        Returns: None
        """
        return self.loggerPath + self.loggerFileName


# logg = Logger()
# print(logg.printInfoMessage("hello world info"))
# print(logg.printErrorMessage("hello world error"))
# print(logg.getLoggerPathAndFilename())


# if not os.path.exists("C:/UC2020/Logs"):
#     os.makedirs("C:/UC2020/Logs/")
# loglevel = 'info'

# logging.basicConfig(filename='C:/UC2020/Logs/example.log', filemode='w',
#                     format='%(asctime)s:%(levelname)s:%(message)s:%(asctime)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# # logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
# logging.warning('Watch out')
# logging.info('I told you so')
# # logging.exception("BIG TROUBLE")
# # t = getattr(logging, loglevel.upper())
# # print(t)
# # logger = logging.getLogger(__name__)
# Logger.exception('BIG TROUBLE')
# # print()
