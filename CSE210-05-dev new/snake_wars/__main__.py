from shared_data import SharedData

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.snake import Snake
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction1
from game.scripting.handle_collisions_action2 import HandleCollisionsAction2
from game.scripting.draw_actors_action import DrawActorsAction
#from game.scripting.grow_tail import GrowTail
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point
from game.scripting.control_actor2_action import ControlActor2Action
from game.services.sound_manager import SoundManager


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("snake1", Snake(1))
    cast.add_actor("snake2", Snake(2))
    cast.add_actor("scores", Score())
   
   
    _data = SharedData()
    _snd_mgr = SoundManager()
    
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("input", ControlActor2Action(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction1())
    script.add_action("update", HandleCollisionsAction2())
    #TODO: finish implementing the below action to extend the players tail as the game progresses.
    #script.add_action("update", GrowTail())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)
    _snd_mgr.play_sound(f'{_data.fs_utils.get_cwd()}{_data.fs_utils.get_os_path_sep()}data{_data.fs_utils.get_os_path_sep()}sounds{_data.fs_utils.get_os_path_sep()}game-over.wav')

if __name__ == "__main__":
    main()