from manimlib.imports import *

class rec(Scene):
    def construct(self):
        text = TexMobject("Okay")
        self.play(
            Write(text)
        )