from manimlib.imports import *
from math import *
import numpy
class timestable(Scene):
    CONFIG = {
            "colors" : [DARK_BLUE, YELLOW],
    }
    def ll(self, circ, x, y = 200):
        lines = VGroup()
        for i in range(y):
            lines.add(Line(circ.point_from_proportion((i%y) / y), circ.point_from_proportion(((i * x) % y) / y), stroke_width=0.7))
        lines.set_color_by_gradient(*self.colors)
        return lines
    def construct(self):
        mod_val = 300
        r = FRAME_HEIGHT*0.9 / 2
        x_ = []
        y_ = []
        times = 200
        tx = TextMobject("")
        lines = VGroup()
        circ = Circle().set_height(FRAME_HEIGHT * 0.9)
        texo = TextMobject("2   Times $\mod$").scale(0.5)
        for m in numpy.arange(10, mod_val + 2, 2):
            x_.clear()
            y_.clear()
            for x in numpy.arange(1, m + 1, 1):
                x_.append(r * cos(x * 2 * PI / m))
                y_.append(r * sin(x * 2 * PI / m))
            
            circle = VGroup()
            for x, y in zip(x_, y_):
                circle.add(Dot(np.array([x,y,0]), color=RED, radius=0.015))

            lines = VGroup()
            colorS = color_gradient([DARK_BLUE, YELLOW], m)
            for i in numpy.arange(0, m, 1):
                j = (i * 2) % m
                lines.add(Line(np.array([x_[i], y_[i], 0]), np.array([x_[int(j)], y_[int(j)], 0]), color=colorS[i], stroke_width=0.7))
            tex1 = DecimalNumber(m).scale(0.5)
            group = VGroup(texo, tex1).arrange_submobjects(RIGHT).to_corner(RIGHT + DOWN)
            self.add(group)
            self.add(circle)
            if m == 10:
                self.play(ShowCreation(circle))
                self.wait(1)
            self.add(lines)
            if m == 10:
                self.play(ShowCreation(lines), run_time=2)
            self.wait(2/60)
            if m < mod_val:
                self.remove(lines)
            if m < mod_val:
                self.remove(circle)
            self.remove(group)
        self.wait(1)
        self.remove(lines)
        texo1 = TextMobject("      Times $\mod 300$")
        tex2 = DecimalNumber(2)
        group = VGroup(tex2, texo1).arrange_submobjects(RIGHT).scale(0.5).to_corner(RIGHT + DOWN)
        
        mod_t = ValueTracker(2)
        tex2.add_updater(lambda v: v.set_value(mod_t.get_value()))
        lins = self.ll(circ, mod_t.get_value(), mod_val)
        
        lins.add_updater(
            lambda obj: obj.become(
                self.ll(circ, mod_t.get_value())
            )
        )
        self.add(group, lins)
        self.play(mod_t.set_value, 200, rate_func=linear, run_time=180)

