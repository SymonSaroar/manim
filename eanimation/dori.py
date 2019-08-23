from manimlib.imports import *
from math import *

class fr(Scene):
    def construct(self):
        text1 = TextMobject("{\\small When the boy is not moving on the rope,}")
        text2 = TextMobject("{\\small it takes all of the boy's weight.}")
        text3 = TextMobject("{\\small Hence the rope feels a Tension equal to the boy's weight}")
        
        text = VGroup(text1, text2, text3).arrange(DOWN)
        text.scale(0.65)
        text.to_corner(UP + LEFT)
        line = Line(2.475 * UP, 3 * DOWN)
        boy = Annulus(inner_radius = 0.01, outer_radius = 0.4, color = RED)
        m = TextMobject("{\\small m")
        m.move_to(boy).set_color(GOLD)
        boyt = TextMobject("{\\small boy}")
        boyt.shift(2 * LEFT + 0.5 * UP)
        ar = Arrow(boyt.get_center(), boy.get_center(), buff = 0.5)
        mg = Arrow(boy.get_center() + RIGHT * 0.25, boy.get_center() + RIGHT * 0.25 + DOWN * 3)
        mgt = TextMobject("{\\small $mg$}")
        mgt.next_to(mg, RIGHT)

        self.play(
            
            ShowCreation(line),
            ShowCreation(boy),
        )
        self.wait()
        self.play(
            Write(text),
            Write(boyt),
            Write(m),
            ShowCreation(ar),
            ShowCreation(mg),
            Write(mgt),
        )
        self.wait(2)
        self.play(FadeOut(text))
        text1 = TextMobject("{\\small Because the Earth is pulling him with}")
        text2 = TextMobject("{\\small a acceleration of $ g = 9.8 $}")
        text = VGroup(text1, text2).arrange(DOWN).scale(0.75)
        text.to_edge(RIGHT)

        T = Arrow(boy.get_center(), boy.get_center() + UP * 2.5).set_color(BLUE)
        Tt = TextMobject("{\\small $T$}","{$=$}")
        Tt.next_to(T, RIGHT)
        self.play(
            Write(text),
            FadeOut(boyt),
            FadeOut(ar),
        )
        self.wait()
        self.play(
            Write(Tt),
            LaggedStart(TransformFromCopy(mg, T),
            ApplyMethod(mgt.next_to, Tt, RIGHT),
            FadeOut(mg))
        )
        text1 = TextMobject("{\\small This ts the maximum tension for the rope}")
        text1.scale(0.75)
        self.wait()
        self.play(
            Write(text1.to_corner(LEFT + UP)),
            FadeOutAndShiftDown(text, RIGHT)
        )
        self.wait()
        text2 = TextMobject("{\\small As the boy starts falling down,}")
        text3 = TextMobject("{\\small he releases tension from the rope.}")
        text = VGroup(text2, text3).arrange(DOWN).scale(0.75)
        text.to_corner(LEFT + UP)
        a = Arrow(boy.get_center() + LEFT * 0.25, boy.get_center() + LEFT * 0.25 + DOWN * 1.5)
        at = TextMobject("{\\small $a$}")
        at.next_to(a, LEFT)
        self.play(
            FadeOut(text1),
            GrowFromCenter(text),
            GrowFromPoint(a, boy.get_center() + LEFT * 0.25),
            FadeIn(at)
        )
        text2 = TextMobject("{\\small So as his acceleration $a$ increases Tension $T$ decreases,}")
        text2.to_corner(UP + LEFT)
        self.play(FadeOut(mgt))
        mgt = TextMobject("{\\small $m$}","{\\small $(g-$}", "{\\small $a$}", "{\\small $)$}")
        mgt.next_to(Tt, RIGHT)
        mgt[2].set_color(GREEN)
        self.play(
            TransformFromCopy(at, mgt),
            ApplyMethod(at.set_color, GREEN),
        )
        boy_ = Annulus(inner_radius = 0.01, outer_radius = 0.4, color = RED)
        boy_.shift(DOWN)
        m_ = TextMobject("{\\small m")
        m_.move_to(boy_).set_color(GOLD)
        a_ = Arrow(boy_.get_center() + LEFT * 0.25, boy_.get_center() + LEFT * 0.25 + DOWN * 2.5)
        T_ = Arrow(boy_.get_center(), boy_.get_center() + UP * 1.5).set_color(BLUE)
        at_ = TextMobject("$a$")
        at_.next_to(a_, LEFT)
        mgt_ = TextMobject("$a$")
        mgt_.move_to(mgt[2])
        Tt_ = TextMobject("{\\tiny $T$}")
        Tt_.next_to(T, RIGHT)
        gr = VGroup(line, a, T, at, mgt, Tt, m, boy)
        self.wait(2)
        self.play(
            FadeOut(text),
            GrowFromCenter(text2),
            Transform(m, m_, run_time = 6),
            Transform(a, a_, run_time = 6),
            Transform(boy, boy_, run_time = 6),
            Transform(T, T_, run_time = 6),
            Transform(at, at_, run_time = 6),
            Transform(mgt[2], mgt_, run_time = 6),
            Transform(Tt[0], Tt_, run_time = 6),
        )
        
        self.wait(1)
        self.play(
            FadeOut(text2),
            ApplyMethod(gr.scale, 0.6,run_time = 0.5),
        )
        self.play(ApplyMethod(gr.to_corner, UP + LEFT))
        t1 = TexMobject("T = m(g - a) = 306")
        t2 = TexMobject("45(9.8 - a) = 306")
        t3 = TexMobject("a = 9.8 - \\displaystyle\\frac {306} {45}")
        t4 = TexMobject("a = 3")
        VGroup(t1, t2, t3, t4).arrange(DOWN).to_edge(RIGHT).shift(LEFT * 2)
        sq = Square()
        sq.surround(t4).set_color(RED)
        self.play(TransformFromCopy(mgt, t1))
        self.wait()
        self.play(TransformFromCopy(t1, t2))
        self.wait()
        self.play(TransformFromCopy(t2, t3))
        self.wait()
        self.play(TransformFromCopy(t3, t4))
        self.wait()
        self.play(ShowCreation(sq, run_time = 1.5))
        self.wait(2)
