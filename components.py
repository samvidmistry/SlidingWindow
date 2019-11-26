from typing import *
from manimlib.imports import *

class TitleAndBulletListLayout:
    @staticmethod
    def createSlide(scene: Scene, title: str, bullet_points: List[str], run_time=1):
        current_object = TextMobject(title)
        current_object.scale(1.2)
        current_object.to_edge(UP)
        scene.play(Write(current_object, run_time=run_time))
        buffer_size = MED_LARGE_BUFF
        for s in bullet_points:
            previous_object = current_object
            current_object = TextMobject(s)
            current_object.scale(0.7)
            dot = Dot()
            dot.next_to(previous_object, direction=DOWN, buff=buffer_size)
            buffer_size = MED_LARGE_BUFF
            dot.to_edge()
            current_object.next_to(dot)
            scene.play(ShowCreation(dot))
            scene.play(Write(current_object, run_time=run_time))

class Utils:
    @staticmethod
    def fadeClearSlide(scene: Scene):
        scene.play(*list(map(FadeOut, scene.mobjects)))

