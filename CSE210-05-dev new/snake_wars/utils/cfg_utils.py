from configparser import ConfigParser
import os
import __main__

from utils.fs_utils import FSUtils

# Create a configuration file, load it, and retrieve values from it. STILL IN DEVELOPMENT.
class ConfigUtils():
    
    # Setup the class:
    def __init__(self):
        self.fs_utils = FSUtils()
        self.configuration = ConfigParser()
        self.default_config = {
            "game_name": "Snake Wars",
            "window_width": 1080,
            "window_height": 720,
            "game_fps": 50,
            "log_level": "DEBUG"
        }
        cwd = self.fs_utils.get_cwd()
        sep = self.fs_utils.get_os_path_sep()
        cfg_dir = f"{cwd}{sep}_config{sep}"
        cfg_filename = "config.ini"
        # Check to see if the config file dir exists. If not, make it.
        if os.path.exists(cfg_dir) == False:
            try: 
                os.mkdir(cfg_dir) 
            except OSError as error: 
                print(error) 
                
        # Check to see if the config file exists. If not, make it and add the default values.  
        if os.path.exists(cfg_dir + cfg_filename) == False:
            try:
                with open(cfg_dir + cfg_filename, 'w') as output_file:
                    self.configuration.add_section("GAME")
                    self.configuration.set("GAME", "game_name", "Snake Wars")
                    self.configuration.set("GAME", "window_width", "1080")
                    self.configuration.set("GAME", "window_height", "720")
                    self.configuration.set("GAME", "game_fps", "15")
                    self.configuration.set("GAME", "log_level", "INFO")
                    self.configuration.write(output_file)
            except OSError as error:
                print(error)
        try:   
            self.configuration.read(cfg_dir + cfg_filename, encoding="utf-8")
        except OSError as error:
            print(error)
        
    # Gets the configuration variable
    def get_cfg(self):
        return self.configuration
    
    # Get a boolean from the configuration file:
    def get_cfg_bool(self, value_var):
        return self.get_cfg().getboolean("GAME", value_var, fallback=None)
    
    # Get a string from the configuration file:
    def get_cfg_string(self, value_var):
        return self.get_cfg().get("GAME", value_var, fallback=None)
    
    # Get an integer from the configuration file:
    def get_cfg_int(self, value_var):
        return self.get_cfg().getint("GAME", value_var, fallback=None)
    
    # Get a float from the configuration file:
    def get_cfg_float(self, value_var):
        return self.get_cfg().getfloat("GAME", value_var, fallback=None)