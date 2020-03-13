from manimlib.imports import *
class test(Scene):
    def construct(self):
        colors = [BLUE, YELLOW, RED]
        circ = Circle().set_height(0.9*FRAME_HEIGHT)
        x = 41
        y = 500
        lines = VGroup()
        for i in range(y):
            lines.add(Line(circ.point_from_proportion((i%y) / y), circ.point_from_proportion(((i * x) % y) / y), stroke_width=0.9))
        lines.set_color_by_gradient(*colors)
        self.add(lines)