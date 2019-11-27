import warnings
from manimlib.imports import *

class TimeTrackingScene(Scene):
    def __init__(self, **kwargs):
        self.current_time = 0.0
        self.timing_file = open("timings.txt", 'w+')
        self.timing_file.write(str(self.current_time) + "\n")
        super(TimeTrackingScene, self).__init__(**kwargs)

    def __del__(self):
        self.timing_file.close()

    def play(self, *args, **kwargs):
        if len(args) == 0:
            warnings.warn("Called Scene.play with no animations")
            return

        animations = self.compile_play_args_to_animation_list(
            *args, **kwargs
        )
        max_runtime = max(list(map(lambda anim: anim.get_run_time(), animations)))
        self.set_current_time(self.get_current_time() + max_runtime)
        self.timing_file.write(str(self.get_current_time()) + "\n")
        Scene.play(self, *args, **kwargs)

    def get_current_time(self):
        return self.current_time

    def set_current_time(self, current_time):
        self.current_time = current_time
