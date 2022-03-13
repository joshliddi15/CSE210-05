import logging
import log21
from log21 import Levels

class LogUtils():
    
    # Initialize the log utils:
    def __init__(self, log_app_name, log_level: int):
        level_names_dict = {log21.WARNING: ' ! ', log21.ERROR: '!!!'}
        self.logger = log21.get_logger(log_app_name, level_names=level_names_dict)
        self.logger.setLevel(level=log_level)
        self.logger.debug("Setup logger...")
    
    # Get the logger variable:
    def get_logger(self):
        return self.logger
    
    # Log a message to the console using the newly created logger:
    def log_msg(self, message_var, msg_level: int):
        if msg_level == Levels.DEBUG:
            self.get_logger().debug(message_var)
        if msg_level == Levels.INFO:
            self.get_logger().info(message_var)
        if msg_level == Levels.WARN:
            self.get_logger().warn(message_var)
        if msg_level == Levels.ERROR:
            self.get_logger().error(message_var)
        if msg_level == Levels.CRITICAL:
            self.get_logger().critical(message_var)
    