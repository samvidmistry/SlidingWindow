from manimlib.imports import *
from components import TitleAndBulletListLayout, Utils

class TestScene(Scene):
    def construct(self):
        title = "Why, bruh?"
        points = [
            "Why should variables be immutable?",
            "No race conditions.",
            "Less cognitive load.",
            "Why should functions be pure?",
            "Concurrency and parallel evaluation.",
            "Why should functions be referentially transparent?",
            "Lazy evaluation."
            ]
        TitleAndBulletListLayout.createSlide(self, title, points)
        Utils.fadeClearSlide(self)
