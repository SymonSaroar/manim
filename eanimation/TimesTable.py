from manimlib.imports import *
from math import *
import numpy
class timestable(Scene):
    CONFIG = {
            "colors" : [DARK_BLUE, YELLOW, RED],
            "times" : 500.01,
    }
    def ll(self, circ, x, y):

        lines = VGroup()
        for i in range(y):
            lines.add(Line(circ.point_from_proportion((i%y) / y), circ.point_from_proportion(((i * x) % y) / y), stroke_width=0.9))
        lines.set_color_by_gradient(*self.colors)
        return lines
    def construct(self):
        mod_val = 500
        r = FRAME_HEIGHT*0.9 / 2
        x_ = []
        y_ = []
        circle = VGroup()
        lines = VGroup()
        group = VGroup()
        circ = Circle().set_height(FRAME_HEIGHT * 0.9)
        texo = TextMobject("$n\\times$").scale(0.5)
        tx = TextMobject("$\\mod$").scale(0.5)
        for m in numpy.arange(10, mod_val + 2, 3):
            x_.clear()
            y_.clear()
            self.remove(lines, circle, group)
            lines = VGroup()
            circle = VGroup()
            for x in numpy.arange(1, m + 1, 1):
                x_.append(r * cos(x * 2 * PI / m))
                y_.append(r * sin(x * 2 * PI / m))
            
            
            for x, y in zip(x_, y_): 
                circle.add(Dot(np.array([x,y,0]), color=RED, radius=(0.025 - m*0.01/500.0)))

            for i in numpy.arange(0, m, 1):  
                j = (i * 2) % m
                lines.add(Line(np.array([x_[i], y_[i], 0]), np.array([x_[int(j)], y_[int(j)], 0]), stroke_width=0.9))
            
            lines.set_color_by_gradient(*self.colors)
            tex1 = DecimalNumber(m).scale(0.5)
            group = VGroup(texo, DecimalNumber(2).scale(0.5), tx, tex1).arrange_submobjects(RIGHT).to_corner(RIGHT + DOWN)
            
            if m == 10:
                self.add(group)
                self.play(ShowCreation(circle))
                self.wait(1)
                self.play(ShowCreation(lines), run_time=2)
            else:
                self.add(group, circle, lines)
            self.wait(1/60)
            
            
        self.wait(1)
       
        self.remove(lines, group)
        tex2 = DecimalNumber(2)
        texo1 = TextMobject("$n\\times$")
        texo2 = TextMobject("$\\mod 500$")
        group = VGroup(texo1, tex2, texo2).arrange_submobjects(RIGHT).scale(0.5).to_corner(RIGHT + DOWN)
        
        mod_t = ValueTracker(2)
        tex2.add_updater(lambda v: v.set_value(mod_t.get_value()))
        group.add_updater(lambda v: v.arrange_submobjects(RIGHT).to_corner(RIGHT + DOWN))
        lins = self.ll(circ, mod_t.get_value(), mod_val)
        
        lins.add_updater(
            lambda obj: obj.become(
                self.ll(circ, mod_t.get_value(), mod_val)
            )
        )
        self.add(group, lins)
        self.play(mod_t.set_value, self.times, rate_func=smooth, run_time=90)
