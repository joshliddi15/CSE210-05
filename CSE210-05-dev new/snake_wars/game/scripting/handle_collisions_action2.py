from shared_data import SharedData
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.services.sound_manager import SoundManager
from log21 import Levels
import math

HIT_RADIUS = 10

class HandleCollisionsAction2(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._data = SharedData()
        self._snd_mgr = SoundManager()

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake = cast.get_first_actor("snake2")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]
        enemy = cast.get_first_actor("snake1")
        enemyTrail = enemy.get_segments()
        head_position = head.get_position()
        cur_x_pos = head_position.get_x()
        cur_y_pos = head_position.get_y()

        
        for segment in segments:
            segment_position = segment.get_position()
            cur_obj_x = segment_position.get_x()
            cur_obj_y = segment_position.get_y()
            if (math.sqrt(((cur_obj_x-cur_x_pos)**2) + ((cur_obj_y-cur_y_pos)**2))) < HIT_RADIUS:
                self._is_game_over = True

        for segment in enemyTrail:
            segment_position = segment.get_position()
            cur_obj_x = segment_position.get_x()
            cur_obj_y = segment_position.get_y()
#todo: move HIT_RADIUS to shared data or something like that. This needs to be done for both handle_collisions_action files.
            if (math.sqrt(((cur_obj_x-cur_x_pos)**2) + ((cur_obj_y-cur_y_pos)**2))) < HIT_RADIUS:
                self._is_game_over = True
#todo: make this message print to the play screen
                print("player1 is the winner")
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if not self._is_game_over:
            return
        snake1 = cast.get_first_actor("snake1")
        snake2 = cast.get_first_actor("snake2")
        segment1 = snake1.get_segments()
        segment2 = snake2.get_segments()

        x = int(self._data.MAX_X / 2)
        y = int(self._data.MAX_Y / 2)
        position = Point(x, y)

        message = Actor()
        message.set_text("Game Over!")
        message.set_position(position)
        cast.add_actor("messages", message)
        self._data.log_utils.log_msg("Game over.", Levels.INFO)
        if self._snd_mgr.sound_playing == False:
            self._snd_mgr.play_sound(f'{self._data.fs_utils.get_cwd()}{self._data.fs_utils.get_os_path_sep()}data{self._data.fs_utils.get_os_path_sep()}sounds{self._data.fs_utils.get_os_path_sep()}game-over.wav')
        for segment in segment1:
            segment.set_color(self._data.WHITE)
        for segment in segment2:
            segment.set_color(self._data.WHITE)