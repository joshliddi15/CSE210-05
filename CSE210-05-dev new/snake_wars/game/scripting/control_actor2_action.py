from shared_data import SharedData
from game.scripting.action import Action
from game.shared.point import Point


class ControlActor2Action(Action):
    """
    An input action that controls the snake that starts on the left.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._data = SharedData()
        self._keyboard_service = keyboard_service
        self._direction = Point(0, -self._data.CELL_SIZE)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('left'):
            self._direction = Point(-self._data.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('right'):
            self._direction = Point(self._data.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('up'):
            self._direction = Point(0, -self._data.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('down'):
            self._direction = Point(0, self._data.CELL_SIZE)
        
        snake = cast.get_first_actor("snake2")
        snake.turn_head(self._direction)
