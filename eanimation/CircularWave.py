from manimlib.imports import *
from math import *

class fr(ThreeDScene):
    CONFIG = {
        "kone": None,
        "rate": None,
        "lines": [],
        "pointt": None,
    }
    def construct(self):
        axes = ThreeDAxes(z_min = 0, z_max = 8,)
        circle = Circle()
        sphere = ParametricSurface(
            lambda u, v: np.array([
                0.2*np.cos(u)*np.cos(v),
                0.2*np.cos(u)*np.sin(v),
                0.2*np.sin(u)
            ]),v_min = 0, v_max = TAU, u_min = -PI / 2, u_max = PI / 2, checkerboard_colors = [RED_D, BLUE_D],
            resolution = (15, 32))
        self.set_camera_orientation(0 * DEGREES)
        sphere.shift(2 * RIGHT)
        self.play(
            ShowCreation(axes),
            ShowCreation(sphere),
        )
        
        
        #Se objects
        self.t_offset=0
        orbit = Circle().scale(2).set_stroke(BLUE, 0.1).set_opacity(0.7)
        

        sphere.move_to(orbit.point_from_proportion(0))

        def update_planet(mob,dt):
            rate = dt*0.2
            mob.move_to(orbit.point_from_proportion(((self.t_offset + rate))%1))
            self.t_offset += rate

        sphere.add_updater(update_planet)
        self.add(sphere)
        self.wait(10)

        self.move_camera(25 * DEGREES, 20 * DEGREES, run_time = 2)
        self.wait(3)
        self.move_camera(0 * DEGREES)
        self.move_camera(90 * DEGREES)
        self.wait(4)
        self.wait(4 * 1 / 60)
        

        self.play(
            ApplyMethod(orbit.shift, 2 * np.array([0, 0, -1])),
            ApplyMethod(axes.shift, 2 * np.array([0, 0, -1]))
        )
        self.move_camera(93.5 * DEGREES, 0)
        ####
       # self.play(
       #     ApplyMethod(axes.shift, 3 * np.array([0,0,-1])),
       #     ApplyMethod(orbit.shift, 3 * np.array([0,0,-1])),
       # )
       # self.move_camera(90 * DEGREES, frame_center = np.array([0, 0, -3]))
        #self.move_camera(180 * DEGREES)
        ###
        wave = ParametricFunction(
            lambda u: np.array([
                0,
                2 * np.sin(u),
                u / 3
            ]), t_min = 0, t_max = 2 * TAU, color = RED_D,
        )
        wave.shift(2 * np.array([0, 0, -1]))
       # wave.shift(3 * np.array([0,0,-1]))
       # self.wait(9/15)
       # def update_wave(mob, dt):
       #     rate = 720 / 75
       #     mob.rotate(-rate * DEGREES, about_point=ORIGIN)
       # wave.add_updater(update_wave)
        def get_angle(mob):
            pp = mob.get_center()
            return acos(pp[0] / sqrt(pp[0] * pp[0] + pp[1] * pp[1] + pp[2] * pp[2])) 
        dot = ParametricSurface(
            lambda u, v: np.array([
                0.05*np.cos(u)*np.cos(v),
                0.05*np.cos(u)*np.sin(v),
                0.05*np.sin(u)
            ]),v_min = 0, v_max = TAU, u_min = -PI / 2, u_max = PI / 2, checkerboard_colors = [BLUE_D, BLUE_D],
            resolution = (15, 32))
        self.kone = 0
        self.rate = 0
        line = DashedLine(dashed_segment_length = 0.5).set_color(BLUE_D)
        self.pointt = np.array([0,0, -2])
        #def update_dot(mob, dt):
        #    self.kone += 720/75
        #    mob.move_to(np.array([0, np.sin(self.kone * DEGREES), -2 + self.kone * DEGREES / 3]))
        
        #dot.add_updater(update_dot)

        line.add_updater(lambda m: m.become(DashedLine(sphere.get_center(), dot.get_center(), dashed_segment_length = 2)))
        
        self.add(dot, line)
        self.play(
            ShowCreation(wave, rate_func = linear, run_time = 1),
            MoveAlongPath(dot, wave, rate_func = linear, run_time = 1),
        )
        sphere.clear_updaters()
        line.clear_updaters()
        self.wait()
        

class sub(ThreeDScene):
    def construct(self):
        dot = ParametricSurface(
            lambda u, v: np.array([
                0.2*np.cos(u)*np.cos(v),
                0.2*np.cos(u)*np.sin(v),
                0.2*np.sin(u)
            ]),v_min = 0, v_max = TAU, u_min = -PI / 2, u_max = PI / 2, checkerboard_colors = [BLUE_D, BLUE_D],
            resolution = (15, 32))
        wave = ParametricFunction(
            lambda u: np.array([
                2 * np.sin(u),
                0,
                u / 3
            ]), t_min = 0, t_max = 2.5 * TAU, color = RED_D,
        )
        axes = ThreeDAxes()
        wave.shift(2 * np.array([0, 0, -1]))
        dot.shift(2 * np.array([0, 0, -1]))
        axes.shift(2 * np.array([0, 0, -1]))
        line = Line(dot.get_center(), np.array([3, 0, 3]))
        
        self.add(axes, wave)
        self.set_camera_orientation(0)
        self.add(line)
        self.wait(2)
        self.move_camera(90 * DEGREES)
        self.play(
            MoveAlongPath(dot, wave)
        )

