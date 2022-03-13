from log21 import Levels
from game.shared.color import Color

from utils.fs_utils import FSUtils
from utils.log_utils import LogUtils
from utils.cfg_utils import ConfigUtils

# Do score managing and other miscellaneous shared functions in here...
class SharedData():
    
    def __init__(self, debug: bool = False):
        self.log_level = Levels.INFO
        self.config_utils = ConfigUtils()
        self.fs_utils = FSUtils()
        self._debug = debug
        self.sound_playing = False
        self.CAPTION = self.config_utils.get_cfg_string("game_name")
        self.log_utils = LogUtils(self.CAPTION, self.log_level)
        self.MAX_X = self.config_utils.get_cfg_int("window_width")
        self.MAX_Y = self.config_utils.get_cfg_int("window_height")
        self.FRAME_RATE = self.config_utils.get_cfg_int("game_fps")
        self.root_dir = self.fs_utils.get_cwd()
        self.path_sep = self.fs_utils.get_os_path_sep()
        self.line_sep = self.fs_utils.get_os_linesep()      
        
        self.COLUMNS = 40
        self.ROWS = 20
        self.CELL_SIZE = 15
        self.FONT_SIZE = 15
        self.SNAKE_LENGTH = 8
        self.WHITE = Color(255, 255, 255)
        self.RED = Color(255, 0, 0)
        self.BLUE = Color(0, 0, 255) # Player 1
        self.PURPLE = Color(170, 0, 255) # Player 2
        self.YELLOW = Color(255, 255, 0)
        self.GREEN = Color(0, 255, 0)
        self.log_utils.log_msg("Done loading shared data.", Levels.DEBUG)
        
    def get_log_level(self):
        if self.config_utils.get_cfg_string("log_level") in ["DEBUG", "DBG"]: 
            self.log_level = Levels.DEBUG
        elif self.config_utils.get_cfg_string("log_level") in ["INFORMATION", "INFO"]: 
            self.log_level = Levels.INFO
        elif self.config_utils.get_cfg_string("log_level") in ["WARNING", "WARN"]: 
            self.log_level = Levels.WARN
        elif self.config_utils.get_cfg_string("log_level") in ["ERROR", "ERR"]: 
            self.log_level = Levels.ERROR
        elif self.config_utils.get_cfg_string("log_level") in ["CRITICAL", "FATAL", "CRIT"]: 
            self.log_level = Levels.CRITICAL
        else:
            self.log_level = Levels.INFO