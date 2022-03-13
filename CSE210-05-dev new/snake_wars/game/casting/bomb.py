import random
from shared_data import SharedData
from game.casting.actor import Actor
from game.shared.point import Point


class Bomb(Actor):
    """
    An object, which, when touched, explodes and insta-kills the player.
    
    The responsibility of Bomb is to select a random position and end the game when it is touched.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        "Constructs a new Bomb."
        super().__init__()
        self._data = SharedData()
        self._points = 0
        self.set_text("!")
        self.set_color(self._data.RED)
        self.reset()
        
    def reset(self):
        """Selects a random position and points that the food is worth."""
        # TODO: #2 Show the game over screen when this runs...
        
    def get_points(self):
        """Gets the points the food is worth.
        
        Returns:
            points (int): The points the food is worth.
        """
        return self._points