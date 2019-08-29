from manimlib.imports import *

class fr(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        sphere = ParametricSurface(
            lambda u, v: np.array([
                0.2*np.cos(u)*np.cos(v),
                0.2*np.cos(u)*np.sin(v),
                0.2*np.sin(u)
            ]),v_min = 0, v_max = TAU, u_min = -PI / 2, u_max = PI / 2, checkerboard_colors = [RED_D, RED_D],
            resolution = (15, 32))
        self.set_camera_orientation(0 * DEGREES)
        #sphere.shift(1.5 * RIGHT)
        self.play(
            ShowCreation(axes),
            ShowCreation(sphere),
        )
        dot = Dot()
        
        #Se objects
        self.t_offset=0
        orbit = Circle().scale(2)
        dot = Dot()

        sphere.move_to(orbit.point_from_proportion(0))

        def update_planet(mob,dt):
            rate=dt*0.4
            mob.move_to(orbit.point_from_proportion(((self.t_offset + rate))%1))
            self.t_offset += rate

        sphere.add_updater(update_planet)
        self.add(sphere)
        self.wait(3)

        self.move_camera(45 * DEGREES, 20 * DEGREES, run_time = 2)
        self.wait(3)
        self.move_camera(90 * DEGREES)
        self.wait(3)
        