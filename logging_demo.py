"""
Examples of using Python's logging facility.

Run the file in Python and observe:
Which messages are actually printed on the console or to a file?
What information is in the message?

For details, see: https://docs.python.org/3/library/logging.html
"""
import logging

def logging_test(logger):
    """Log messages using each of the standard logging levels 
       plus 1 custom log level.
    """ 
    # debug
    logger.debug('Debuging something')
    # info
    logger.info('The result should be {"Roles": "admin"}')
    # warning
    logger.warning('The constant value should be uppercase')
    # level = logging.WARN + 5 (custom log level between WARN and ERROR)
    level = logging.WARN + 5  # custom log level
    logger.log(level, f"This is fail on level {level}")
    # error
    logger.error('Cannot connect to the database')
    # critical or fatal
    logger.critical('File name "data.txt" could not be found')


def simple_config():
    """Configure logging using basicConfig for simple configuration.

    You should call this before creating any logging objects.
    You can call basicConfig only once. 

    Some named attributes you can set using basicConfig are:

        filename = "name of a file to send log messages to"
        filemode = 'a' (append), 'w' (truncate & open for writing)
        format = a string describing format of log messages
        stream = name of a StreamHandler to use, cannot use with filename attribute
        level = the root logger level (threshold level for log msgs)

    See:  help(logging.basicConfig)
    https://docs.python.org/3/library/logging.html#logging.basicConfig
    """
    # use a custom format for log messages
    FORMAT = '%(asctime)s %(name)s %(levelname)s: %(message)s'
    logging.basicConfig(format=FORMAT)


def my_config():
    """Write your own logging configuration."""
    # TODO write your own logging configuration
    #      specify a log file, threshold level, format, and append mode
    FORMAT = '%(name)s %(funcName)s %(levelname)s: %(message)s'
    LEVEL = 8
    logging.basicConfig(format=FORMAT, level=logging.DEBUG + LEVEL,
            filename="mylog.log", filemode='w')


if __name__ == "__main__":
    #
    # TODO Configure logging using one of these choices:

    # 1. Call basicConfig with the default settings
    # logging.basicConfig()

    # 2. Call simple_config to set the format of log messages.
    #    Comment out the above call (#1) to basicConfig for this.
    # simple_config()

    # 3. my_config() write your own logging configuration as
    #    described in the assignment. 
    #    Comment out the above calls to simple_config and basicConfig.
    my_config()

    # Log some messages to the root logger using different logging levels.
    logger = logging.getLogger()
    logger.setLevel(logging.WARN)
    print("Logging to ", str(logger))
    logging_test(logger)
