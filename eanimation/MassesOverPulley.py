from manimlib.imports import *
from math import *

class fr(Scene):
    CONFIG = {
        "rate1": None,
        "rate2": None,
    }
    def construct(self):
        M = TextMobject("\\large M").set_color(YELLOW)
        m = TextMobject("\\small m").set_color(YELLOW)
        Mr = Square().surround(M).set_color(RED_D).set_fill(RED)
        mr = Square().surround(m).set_color(RED_D).set_fill(RED)
        M1 = VGroup(Mr,M)
        M2 = VGroup(mr,m)
        dot = Dot(radius = 0.05)
        dot.move_to(2 * UP)
        circle = Circle(radius = 0.5).set_color(WHITE)
        circle.move_to(dot)
        self.play(
            ShowCreation(dot, run_time = 2)
        )
        self.play(GrowFromCenter(circle))
        line1 = Line(np.array([0.5, 2, 0]), np.array([0.5, -0.5, 0])).set_stroke(width = 2)
        line2 = Line(np.array([-0.5, 2, 0]), np.array([-0.5, -0.5, 0])).set_stroke(width = 2)
        M1.next_to(line1, DOWN, buff = 0)
        M2.next_to(line2, DOWN, buff = 0)
        self.play(
            ShowCreation(M1),
            ShowCreation(M2),
            ShowCreation(line1),
            ShowCreation(line2),
        )
        self.wait(2)
        F1 = Arrow(ORIGIN, 1.5 * DOWN)
        F2 = Arrow(ORIGIN, 1 * DOWN)
        T1 = Arrow(ORIGIN, 1.5 * UP)
        T2 = Arrow(ORIGIN, 1 * UP)
        F1.next_to(M1, DOWN, buff = SMALL_BUFF)
        F2.next_to(M2, DOWN, buff = SMALL_BUFF)
        T1.next_to(M1, UP, buff = 0)
        T2.next_to(M2, UP, buff = 0)
        T1t = TextMobject("\\small $T$")
        T2t = TextMobject("\\small $T$")
        F1t = TextMobject("\\small $Mg$")
        F2t = TextMobject("\\small $mg$")
        T1t.next_to(T1, RIGHT, buff = SMALL_BUFF).set_color(DARK_BLUE)
        T2t.next_to(T2, LEFT, buff = SMALL_BUFF).set_color(DARK_BLUE)
        F1t.next_to(F1, DOWN, buff = SMALL_BUFF).set_color(PURPLE)
        F2t.next_to(F2, DOWN, buff = SMALL_BUFF).set_color(PURPLE)
        self.play(
            GrowFromCenter(F1),
            GrowFromCenter(F2),
            GrowFromCenter(T1),
            GrowFromCenter(T2),
            Write(T1t), Write(T2t), Write(F1t), Write(F2t),
        )
        
        self.wait()
        M1.add_updater(lambda m: m.next_to(line1, DOWN, buff = 0))
        M2.add_updater(lambda m: m.next_to(line2, DOWN, buff = 0))
        T1.add_updater(lambda m: m.next_to(M1, UP, buff = 0))
        T2.add_updater(lambda m: m.next_to(M2, UP, buff = 0))
        F1.add_updater(lambda m: m.next_to(M1, DOWN, buff = SMALL_BUFF))
        F2.add_updater(lambda m: m.next_to(M2, DOWN, buff = SMALL_BUFF))
        T1t.add_updater(lambda m: m.next_to(T1, RIGHT, buff = SMALL_BUFF))
        T2t.add_updater(lambda m: m.next_to(T2, LEFT, buff = SMALL_BUFF))
        F1t.add_updater(lambda m: m.next_to(F1, DOWN, buff = SMALL_BUFF))
        F2t.add_updater(lambda m: m.next_to(F2, DOWN, buff = SMALL_BUFF))
        def func1(mob):
            mob.set_color(MAROON)
            mob.scale(1.3 / 1.5)
            return mob
        def func2(mob):
            mob.set_color(MAROON)
            mob.scale(1.3)
            return mob
        
        def update_line1(mob, dt):
            self.rate1 = dt * 0.0625
            mob.put_start_and_end_on(np.array([0.5, 2, 0]), mob.get_end() - self.rate1 * np.array([0,1,0]))
        
        def update_line2(mob, dt):
            self.rate2 = dt * 0.0625
            mob.put_start_and_end_on(np.array([-0.5, 2, 0]), mob.get_end() - self.rate1 * np.array([0,-1,0]))
        line1.add_updater(update_line1)
        line2.add_updater(update_line2)
        self.play(
            ApplyFunction(func1, T1, rate_func = rush_into),
            ApplyFunction(func2, T2, rate_func = rush_into),
        )
        self.wait(5)
       # F2t.clear_updaters()
        
        T2t.become(TextMobject("\\small $T - mg$"))
       # T1t.clear_updaters()
        
        F1t.become(TextMobject("\\small $Mg - T$"))
        T1.clear_updaters()
        F2.clear_updaters()
        self.play(
            Transform(F2t, T2t),
            Transform(T1t, F1t),
            Transform(T1, F1),
            Transform(F2, T2),
            FadeOut(T1),
            FadeOut(F2),
        )
        self.remove(F2t, T1t)
        self.wait(5)