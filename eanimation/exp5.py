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
        box_.move_to(ORIGIN)
        line_ = Line(6 * LEFT, 6 * RIGHT).rotate(30 * DEGREES).move_to(box_).shift((0.25 / cos(60 * DEGREES)) * RIGHT)

        
        Wtext = TextMobject("\\small $mg$")
        
        self.play(
            Transform(line2_, line_),
            Transform(box, box_),
            FadeOutAndShiftDown(line),
        )
        
        F = Arrow(box.get_center(),box.get_center() + RIGHT * 4, buff = 0).rotate(30 * DEGREES, about_point = box.get_center())
        F_ = Arrow(box.get_center(),box.get_center() + RIGHT * 4).rotate(30 * DEGREES, about_point = box.get_center())
        Fx = Arrow(box.get_center(),box.get_center() + RIGHT * 4, buff = 0, dashed_segment_length = 0.5).rotate(30 * DEGREES, about_point = box.get_center()).set_color(GREEN).set_opacity(0.7)
        Fx_ = Arrow(box.get_center(),box.get_center() + RIGHT * 4).rotate(30 * DEGREES, about_point = box.get_center()).set_color(YELLOW).set_opacity(0.7)
        Fy = Arrow(box.get_center(),box.get_center() + RIGHT * 4, buff = 0, dashed_segment_length = 0.5).rotate(120 * DEGREES, about_point = box.get_center()).set_color(GREEN).set_opacity(0.7)
        Fy_ = Arrow(box.get_center(),box.get_center() + RIGHT * 4).rotate(120 * DEGREES, about_point = box.get_center()).set_color(ORANGE).set_opacity(0.7)
        p2 = Fx.get_end()
        p3 = Fy.get_end()
        Fy.put_start_and_end_on(box.get_center(), (box.get_center() + (p3 - box.get_center()) * ((3*sin(30 * DEGREES)) / 3)))
        Ft = TextMobject("\\small F")
        Fxt = TextMobject("\\tiny F$\\cos{60^{\\circ}}$")
        Fyt = TextMobject("\\tiny F$\\sin{60^{\\circ}}$")
        Fxt_ = TextMobject("\\tiny F$\\cos{60^{\\circ}}$")
        Fyt_ = TextMobject("\\tiny F$\\sin{60^{\\circ}}$")
        Ft.next_to(F, UP)
        Fxt.next_to(Fx, UP, buff = -0.8)
        Fyt.next_to(Fy, LEFT, buff = -0.25)
        self.play(
            Write(Ft),
            ShowCreation(F),
            ShowCreation(Fx),
            
        )
        self.wait()
        scl1 = ((3*cos(60 * DEGREES)) / 3)
        scl2 = ((3*sin(60 * DEGREES)) / 3)
        ft = Arc(30 * DEGREES, 60 * DEGREES, arc_center = box.get_center(), radius = 0.75)
        ft.add_tip(0.15)
        ft_t = TextMobject("\\tiny $60^{\\circ}$")
        ft_t.next_to(ft, UP + RIGHT, buff = -0.15)
        ft_t.shift(0.15 * UP + 0.2 * LEFT)
        
        self.play(
            Write(Fxt),
            Write(Fyt),
            Write(ft_t),
            ShowCreation(ft, run_time = 1.5),
            Rotating(F, radians = 60 * DEGREES, run_time = 1, about_point = box.get_center()),
            ApplyMethod(Fy.put_start_and_end_on, box.get_center(), (box.get_center() + (p3 - box.get_center()) * scl2), run_time = 1),
            ApplyMethod(Fx.put_start_and_end_on, box.get_center(), (box.get_center() + (p2 - box.get_center()) * scl1), run_time = 1),
        )
        
        self.play(ApplyMethod(F.set_opacity, 0.35))
        W = Arrow(box.get_center(), box.get_center() + DOWN * 2.5)
        Wx = Arrow(box.get_center(), box.get_center() + DOWN * 2.5).set_color(BLUE)
        Wx_ = Arrow(box.get_center(), box.get_center() + DOWN * 2.5).rotate(30 * DEGREES, about_point = box.get_center()).set_color(BLUE)
        Wy = Arrow(box.get_center(), box.get_center() + DOWN * 2.5).set_color(BLUE)
        Wy_ = Arrow(box.get_center(), box.get_center() + DOWN * 2.5).rotate(300 * DEGREES, about_point = box.get_center()).set_color(BLUE)
        Wtext.next_to(W, DOWN)
        self.add(Wtext)
        p2 = Wx_.get_end()
        p3 = Wy_.get_end()
        scl1 = (cos(30 * DEGREES))
        scl2 = (sin(30 * DEGREES))
        wt = Arc(270 * DEGREES, 30 * DEGREES, arc_center = box.get_center(), radius = 0.75)
        wt.add_tip(0.15)
        wt_t = TextMobject("\\tiny $30^{\\circ}$")
        wt_t.next_to(wt, DOWN)
        wt_t.scale(0.75)
        wt_t.shift(0.1*RIGHT + 0.2 * UP)
        Wxt = TextMobject("\\tiny $mg\\sin{30^{\\circ}}$")
        Wyt = TextMobject("\\tiny $mg\\cos{30^{\\circ}}$")
        Wxt.next_to(Wx, UP)
        Wxt.shift(LEFT)
        Wxt.shift(0.35 * LEFT + 0.4 * DOWN)
        Wyt.next_to(Wy,RIGHT)
        Wyt.shift(0.2 * RIGHT + 0.4 * DOWN)
        self.play(
            Write(Wxt),
            Write(Wyt),
            Write(wt_t),
            ShowCreation(wt),
            TransformFromCopy(Wx, Wx_),
            TransformFromCopy(Wy, Wy_),
            ApplyMethod(Wx_.put_start_and_end_on, box.get_center(), (box.get_center() + (p2 - box.get_center()) * scl1)),
            ApplyMethod(Wy_.put_start_and_end_on, box.get_center(), (box.get_center() + (p3 - box.get_center()) * scl2)),
            FadeOut(Wx, run_time = 0.25),
            FadeOut(Wy, run_time = 0.25),
            ApplyMethod(W.set_opacity, 0.35)
        )
        R = Arrow(box.get_center(), Fy.get_vector() + Wx_.get_vector() + box.get_center(), buff = 0).set_color(RED)
        self.wait()
        self.play(
            Indicate(Fy),
            Indicate(Wx_),
        )
        self.play(
            TransformFromCopy(VGroup(Fy, Wx_), R),
            FadeOut(VGroup(Fy, Wx_)),
            FadeOut(Fyt),
            FadeOut(Wyt),
            FadeOut(wt),
            FadeOut(wt_t),
        )
        Rt = TextMobject("\\small $R = F\\sin{60^{\\circ}} - mg\\cos{30^{\\circ}}$")
        Rt.next_to(R, UP).set_color(RED).shift(0.5 * LEFT)
        self.play(
            Write(Rt),
        )
        self.wait()
        Acf = Arrow(box.get_center(), Fx.get_vector() + Wy_.get_vector() + box.get_center(), buff = 0).set_color(GREEN)
        
        self.play(
            Indicate(Fx),
            Indicate(Wy_),
        )
        Acft = TextMobject("\\small $F\\cos{60^{\\circ}} - mg\\sin{30^{\\circ}}$")
        Acft.next_to(Acf, RIGHT).set_color(GREEN)
        self.play(
            TransformFromCopy(VGroup(Fx, Wy_), Acf),
            FadeOut(VGroup(Fx, Wy_)),
            FadeOut(Fxt),
            TransformFromCopy(Wxt, Acft),
            FadeOut(Wxt),
            FadeOut(ft_t),
            FadeOut(ft),
        )
        self.wait()
        gr = VGroup(box, line2_, F, W, Acf, Acft, R, Rt, Ft, Wtext)
        self.play(
            ApplyMethod(gr.scale, 0.5)
        )
        self.play(
            ApplyMethod(gr.to_corner, UP + LEFT)
        )
        
        line = Line(3 * LEFT + 2 * DOWN , 3 * RIGHT + 2 * DOWN)
        box2 = Rectangle(height = 0.5, width = 1, color = RED)
        box2.move_to(line)
        box2.shift(0.25*UP)
        
        self.play(
            ShowCreation(line),
            ShowCreation(box2),
        )
        Fr = Arrow(box2.get_center(), box2.get_center() + 3 * LEFT, buff = 0)
        Frt = TextMobject("\\tiny    = $\\mu * R $")
        Frt.next_to(Fr, UP)
        Rr = Arrow(box2.get_center(), box2.get_center() + 2 * DOWN, buff = 0)
        Rrt = TextMobject("\\tiny $R$")
        Rrt.next_to(Rr, RIGHT)
        self.play(
            ShowCreation(Fr),
            ShowCreation(Rr),
            ShowCreation(Rrt),
            ShowCreation(Frt),
        )
        gr2 = VGroup(line, box2, Fr, Frt, Rr, Rrt)
        def scaleup(mob):
            mob.scale(2)
            mob.move_to(ORIGIN)
            return mob
        def scaledown(mob):
            mob.scale(0.5)
            mob.to_corner(UR)
            return mob
        self.wait(2)
        self.play(
            ApplyFunction(scaleup, gr),
            ApplyFunction(scaledown, gr2),
        )
        self.wait()
        Fs = Arrow(box.get_center(), box.get_center() + 1 * RIGHT, buff = 0).rotate(210 * DEGREES, about_point = box.get_center())
        Fst = TextMobject("\\tiny $F_s = \\mu (-R)$")
        Fst.next_to(Fs, UP)
        Fst.shift(LEFT)
        Fst.shift(0.5 * LEFT + 0.4 * DOWN)
        self.play(
            Write(Fst),
            ShowCreation(Fs),
        )
        self.wait()
        gr.add(Fs, Fst)
        def scaledown2(mob):
            mob.scale(0.5)
            mob.to_corner(UL)
            return mob
        self.play(
            ApplyFunction(scaledown2, gr),
        )

        T1 = TexMobject("\\small \\mu (-R) = F\\cos{60^{\\circ}} - mg\\sin{30^{\\circ}}")
        T2 = TexMobject("\\small \\mu","\\small (-(F\\sin{60^{\\circ}} - mg\\cos{30^{\\circ}}))","\\small = ", "\\small F\\cos{60^{\\circ}} - mg\\sin{30^{\\circ}}")
        T3 = TexMobject("\\small 0.5","\\small (-F\\sin{60^{\\circ}} + \\displaystyle \\frac{2.5 \\cdot 9.8 \\cdot \\sqrt{3}}{2})","\\small = ", "\\small F\\cos{60^{\\circ}} - \\displaystyle \\frac{2.5 \\cdot 9.8}{2}")
        T4 = TexMobject("\\small -0.5 F\\sin{60^{\\circ}} - F\\cos{60^{\\circ}} = - 12.25 - 0.5 \\cdot 2.5 \\cdot 9.8 \\cdot\\displaystyle \\frac{\\sqrt{3}}{2} ")
        T5 = TexMobject("\\small F = \\displaystyle \\frac{-12.25 - 10.284}{-0.5\\sin{60^{\\circ}} - \\cos{60^{\\circ}}}")
        T6 = TexMobject("\\small F = \\displaystyle\\frac{-22.534}{-0.933} = 24.15 N")
        VGroup(T1, T2, T3, T4, T5, T6).arrange(DOWN).scale(0.7).shift(0.5 * RIGHT + DOWN)
        self.play(
            TransformFromCopy(VGroup(Fst, Acft), T1)
        )
        self.wait()
        self.play(FadeInFrom(T2, UP))
        self.wait()
        self.play(
            FadeInFrom(T3, UP)
        )
        self.wait()
        self.play(FadeInFrom(T4, UP))
        self.wait()
        self.play(FadeInFrom(T5, UP))
        self.wait()
        self.play(FadeInFrom(T6, UP))
        sq = Rectangle()
        sq.surround(T6).set_color(RED)
        self.play(FadeToColor(T6, RED))
        self.wait()