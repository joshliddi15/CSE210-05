from shared_data import SharedData
from game.casting.actor import Actor
from game.shared.point import Point


class Snake(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, player_num):
        super().__init__()
        self._data = SharedData()
        self._segments = []
        self._player_num = player_num
        self._prepare_body()

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for _ in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            # TODO: #5 Use the below code (or pseudo-code) to change the player's color based on the player #:
            # if self._player_num == 1:
            #     segment.set_color(self._data.BLUE)
            # else:
            #     segment.set_color(self._data.PURPLE)
            segment.set_color(self._data.BLUE)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        if self._player_num == 1:
            x = int(self._data.MAX_X / 10)
            y = int(self._data.MAX_Y / 2)
        elif self._player_num == 2:
            x = int(self._data.MAX_X / 2)
            y = int(self._data.MAX_Y / 2)

        for i in range(self._data.SNAKE_LENGTH):
            position = Point(x - i * self._data.CELL_SIZE, y)
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
            self._segments.append(segment)