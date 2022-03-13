from multiprocessing.shared_memory import ShareableList
from game.scripting.action import Action
from log21 import Levels
from shared_data import SharedData

class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service
        self._data = SharedData()

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score = cast.get_first_actor("scores")
        snake1 = cast.get_first_actor("snake1")
        snake2 = cast.get_first_actor("snake2")
        segment1 = snake1.get_segments()
        segment2 = snake2.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actors(segment1)
        self._video_service.draw_actors(segment2)
        self._video_service.draw_actor(score)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()
        self._data.log_utils.log_msg("Drew actors.", Levels.DEBUG)