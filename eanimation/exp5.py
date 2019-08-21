from manimlib.imports import *
from math import *

class fr(Scene):
    def construct(self):
        line = Line(6 * LEFT + 3 * DOWN , 6 * RIGHT + 3 * DOWN)
        line2_ = Line(6 * LEFT + 3 * DOWN, 6 * RIGHT + 3 * DOWN)
        line2_.rotate(30 * DEGREES, about_point = line.get_edge_center(LEFT))
        box = Rectangle(height = 0.5, width = 1, color = RED)
        box_ = Rectangle(height = 0.5, width = 1, color = RED)
        box_.next_to(line, UP)
        box_.shift(0.25 * DOWN)
        box_.rotate(30 * DEGREES, about_point = line.get_edge_center(LEFT))
        box.next_to(line, UP)
        box.shift(0.25 * DOWN)
        self.play(
            ShowCreation(line, run_time = 0.5),
            ShowCreation(box)
        )
        self.play(
            TransformFromCopy(line, line2_, run_time = 0.5),
            Transform(box, box_, run_time = 0.5)
        )
        self.wait()
        p1 = box_.get_center()
        box_.move_to(ORIGIN + DOWN)
        line_ = Line(100 * LEFT, 100 * RIGHT).rotate(30 * DEGREES).move_to(box_).shift((0.25 / cos(60 * DEGREES)) * RIGHT)

        
        Wtext = TextMobject("$mg$")
        
        self.play(
            Transform(line2_, line_),
            Transform(box, box_),
            FadeOutAndShiftDown(line),
        )
        
        F = Arrow(box.get_center(),box.get_center() + RIGHT * 3).rotate(30 * DEGREES, about_point = box.get_center())
        F_ = Arrow(box.get_center(),box.get_center() + RIGHT * 3).rotate(30 * DEGREES, about_point = box.get_center())
        Fx = Arrow(box.get_center(),box.get_center() + RIGHT * 3, dashed_segment_length = 0.5).rotate(30 * DEGREES, about_point = box.get_center()).set_color(GREEN).set_opacity(0.7)
        Fx_ = Arrow(box.get_center(),box.get_center() + RIGHT * 3).rotate(30 * DEGREES, about_point = box.get_center()).set_color(YELLOW).set_opacity(0.7)
        Fy = Arrow(box.get_center(),box.get_center() + RIGHT * 3, dashed_segment_length = 0.5).rotate(120 * DEGREES, about_point = box.get_center()).set_color(GREEN).set_opacity(0.7)
        Fy_ = Arrow(box.get_center(),box.get_center() + RIGHT * 3).rotate(120 * DEGREES, about_point = box.get_center()).set_color(ORANGE).set_opacity(0.7)
        p2 = Fx.get_end()
        p3 = Fy.get_end()
        Fy.put_start_and_end_on(box.get_center(), (box.get_center() + (p3 - box.get_center()) * ((3*sin(30 * DEGREES)) / 3)))
        self.play(
            ShowCreation(F),
            ShowCreation(Fx),
        )
        for i in range(30, 61, 30):
            scl1 = ((3*cos(i * DEGREES)) / 3)
            scl2 = ((3*sin(i * DEGREES)) / 3)
            if i == 30:
                self.play(
                    ApplyMethod(F.set_opacity, 0.5),
                    ApplyMethod(F.rotate, 30 * DEGREES, {"about_point": box.get_center()}),
                    
                    ShowCreation(Fy),
                    ApplyMethod(Fx.put_start_and_end_on, box.get_center(), (box.get_center() + (p2 - box.get_center()) * scl1)),
                )
            else:
                self.play(   
                    ApplyMethod(F.set_opacity, 0.25), 
                    ApplyMethod(F.rotate, 30 * DEGREES, {"about_point": box.get_center()}),
                    
                    ApplyMethod(Fy.put_start_and_end_on, box.get_center(), (box.get_center() + (p3 - box.get_center()) * scl2)),
                    ApplyMethod(Fx.put_start_and_end_on, box.get_center(), (box.get_center() + (p2 - box.get_center()) * scl1)),
                )
        self.play(ApplyMethod(F.set_opacity, 0.5))
        W = Arrow(box.get_center(), box.get_center() + DOWN * 2)
        Wx = Arrow(box.get_center(), box.get_center() + DOWN * 2).set_color(BLUE)
        Wx_ = Arrow(box.get_center(), box.get_center() + DOWN * 2).rotate(30 * DEGREES, about_point = box.get_center()).set_color(BLUE)
        Wy = Arrow(box.get_center(), box.get_center() + DOWN * 2).set_color(BLUE)
        Wy_ = Arrow(box.get_center(), box.get_center() + DOWN * 2).rotate(300 * DEGREES, about_point = box.get_center()).set_color(BLUE)
        Wtext.next_to(W, RIGHT)
        self.add(Wtext)
        p2 = Wx_.get_end()
        p3 = Wy_.get_end()
        scl1 = (cos(30 * DEGREES))
        scl2 = (sin(30 * DEGREES))
        self.play(
            TransformFromCopy(Wx, Wx_),
            TransformFromCopy(Wy, Wy_),
            ApplyMethod(Wx_.put_start_and_end_on, box.get_center(), (box.get_center() + (p2 - box.get_center()) * scl1)),
            ApplyMethod(Wy_.put_start_and_end_on, box.get_center(), (box.get_center() + (p3 - box.get_center()) * scl2)),
            FadeOut(Wx, run_time = 0.25),
            FadeOut(Wy, run_time = 0.25),
            ApplyMethod(W.set_opacity, 0.5)
        )
        