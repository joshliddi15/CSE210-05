from game.scripting.action import Action
from shared_data import SharedData
from game.casting.actor import Actor
from game.shared.point import Point


class GrowTail(Action):
    """
    An update action that extends a players trail.
    
    The responsibility of GrowTail is to increase the trail length of each cycle to make the game progressively more difficult
    """

    def execute(self, cycle):
        """Executes the move actors action.

        Args:
            cycle (Snake): The cycle which will have it's tail extended

        """
#position of new segment is end segment location minus cell_size in direction of end segment velocity. This will make the tail extend in the direction it is already going.
#we also need to make a counter somewhere so that we can have the tail grow every X frames. This will make it so the tail doesn't just grow like crazy out of control.

        position = Point(x, y)
        velocity = Point(1 * self._data.CELL_SIZE, 0)
        text = "8" if i == 0 else "#"
        if self._player_num == 1:
            color = self._data.YELLOW if i == 0 else self._data.GREEN
        elif self._player_num == 2:
            color = self._data.RED if i == 0 else self._data.PURPLE
        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text(text)
        segment.set_color(color)
        cycle._segments.append(segment)