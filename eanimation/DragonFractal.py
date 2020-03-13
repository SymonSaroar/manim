from manimlib.imports import *

class Dragon(MovingCameraScene):
    CONFIG = {
        "iterations":5,
        "colors":[DARK_RED, YELLOW],
    }
    def construct(self):
        path = VGroup()
        line = Line(ORIGIN,UP / 10).set_color(DARK_RED)
        path.add(line)

        self.camera_frame.set_height(line.get_height() * 1.2)
        self.camera_frame.move_to(line)
        self.play(ShowCreation(line))

        self.target_path = self.allP(path,self.iterations)
        for i in range(self.iterations):
            path.set_color_by_gradient(*self.colors)
            self.dup(path,i)
        #####
        ## Have to add flipper for twinDragon
        ####
        self.wait()

    def dup(self,path,i):
        set_paths = self.target_path[:2**(i + 1)]
        height = set_paths.get_height() * 1.1
        new_P = path.copy()
        self.add(new_P)
        point = self.getP(path)
        self.play(
            Rotating(
                new_P,
                radians=PI/2,
                about_point=path[-1].points[point],
                rate_func=linear
                ),
            self.camera_frame.move_to,set_paths,
            self.camera_frame.set_height,height,
            run_time=1, rate_func=smooth
            )
        newP = reversed([*new_P])
        path.add(*newP)

    def allP(self, path, iterations):
        target_path = path.copy()
        for _ in range(iterations):
            new_P = target_path.copy()
            point = self.getP(new_P)
            new_P.rotate(
                        PI/2, 
                        about_point=target_path[-1].points[point],
                    )
            newP = reversed([*new_P])
            target_path.add(*newP)

        return target_path

    def getP(self, path):
        return 0 if len(path) > 1 else -1