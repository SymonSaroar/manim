from manimlib.imports import *
from math import *

class fr(Scene):
    def construct(self):
        ball = Circle()
        ball.scale(0.25)
        ball.shift(3.46 * DOWN + 2 * LEFT)
        surface = Line(8 * LEFT, 8 * RIGHT)
        surface.rotate(90 * DEGREES)
        surface.shift(4 * LEFT + ball.get_edge_center(LEFT) - ball.get_center())
        X = np.arange(-4, 4.1, 0.5)
        lines = []
        for x in X:
            lines.append(Line(np.array([-4.25, x, 0]), np.array([-4.45, x - 0.15, 0])))
        self.play(
            ShowCreation(surface),
            ShowCreation(lines[0]),
            ShowCreation(lines[1]),
            ShowCreation(lines[2]),
            ShowCreation(lines[3]),
            ShowCreation(lines[4]),
            ShowCreation(lines[5]),
            ShowCreation(lines[6]),
            ShowCreation(lines[7]),
            ShowCreation(lines[8]),
            ShowCreation(lines[9]),
            ShowCreation(lines[10]),
            ShowCreation(lines[11]),
            ShowCreation(lines[12]),
            ShowCreation(lines[13]),
            ShowCreation(lines[14]),
            ShowCreation(lines[15]),
            ShowCreation(lines[16]),
        )
        self.wait()
        
        self.add(ball)
        t1 = TextMobject("v1")
        t2 = TextMobject("v2")
        v1 = Arrow(ball.get_center(), np.array([-4, 0, 0]), buff = 0.5).set_color(BLUE)
        t1.next_to(v1, DOWN).shift(0.15*UP)
        v2 = Arrow(np.array([-4, 0, 0]), np.array([-2, 3.46, 0]), buff = 0.5).set_color(GREEN)
        t2.next_to(v2, UP).shift(0.15 * DOWN)
        ca1 = CurvedArrow(v1.get_center(), v2.get_center())
        ca1.shift(0.25 * LEFT)
        ca1.scale(0.75)
        t3 = TexMobject("\\theta")
        t3.next_to(ca1)
       # v1.rotate(300 * DEGREES, about_point = ball.get_center())
        ball.get_edge_center(RIGHT)
        self.play(
            ShowCreation(v1),
            ApplyMethod(ball.move_to, np.array([-4, 0, 0])),
            Write(t1),
        )
        self.play(
            ShowCreation(v2),
            ApplyMethod(ball.move_to, np.array([-2, 3.46, 0])),
            Write(t2),
        )
        text = TextMobject("{\\small What is the angle between v1 and v2?}")
        text_ = TextMobject("{\\small Note that, v1 and v2 are vectors.}")
        tex = VGroup(text, text_).arrange(DOWN).to_edge(RIGHT)
        text = TextMobject("{\\small Is this the angle?}")
        self.play(Write(tex))
        self.wait(2)
        self.play(
            FadeOut(tex),
            Write(text),
            ShowCreation(ca1),
            Write(t3),
        )
        self.wait()
        self.play(
            ApplyMethod(v1.put_start_and_end_on, v2.get_end(), v2.get_start()),
            ApplyMethod(v2.set_opacity, 0.5),
        )
        text_ = TextMobject("{\\large \\textbf NOPE}").set_color(RED)
        self.play(
            WiggleOutThenIn(v1, scale_value = 1.5, rotation_angle = 0.02 * TAU, n_wiggles = 6),
            FadeOutAndShiftDown(text),
            GrowFromCenter(text_)
        )
        self.wait()
        v1_ = Arrow(np.array([-2, -3.46, 0]), np.array([-4, 0, 0]), buff = 0.5).set_color(BLUE)
        self.play(
            FadeOut(text_),
            Uncreate(ca1),
            FadeOut(t3),
            Transform(v1, v1_),
            ApplyMethod(v2.set_opacity, 1)
        )
        
        ll = DashedLine(np.array([-4, 0, 0]) , np.array([-6.01, 3.49, 0]), dashed_segment_length = .5, buff = 0.5)
        ll.add_tip(0.2)
        ca2 = Arc(60 * DEGREES, 60 * DEGREES, arc_center = np.array([-4, 0, 0]), radius = 2)
        ca2.add_tip(0.3, True)
        t3.next_to(ca2, UP)
        self.play(
            GrowFromPoint(ll, np.array([-4, 0, 0])),
            FadeOut(ca1),
            GrowFromCenter(ca2),
            FadeIn(t3),
        )
        self.wait()
        self.play(
            ApplyMethod(ll.rotate, -60 * DEGREES, {"about_point": np.array([-4, 0, 0])}),
            ApplyMethod(v2.set_opacity, 0.5),
        )
        self.play(
            Indicate(ll, run_time = 1),
        )
        self.wait()
        text = TextMobject("So,", "this $\\theta$", "{\\small is the the angle between v1 and v2}")
        text[1].set_color(RED)
        VGroup(text[0], text[1], text[2]).arrange(DOWN).to_edge(RIGHT)

        self.play(Write(text[0]))
        self.play(
            Rotating(ll, radians = 60 * DEGREES, run_time = 1, about_point = np.array([-4, 0, 0])),
            TransformFromCopy(t3, text[1]),
            Write(text[2]),
        )