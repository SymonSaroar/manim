from manimlib.imports import *

class fr(Scene):
    def construct(self):
        title = TextMobject("FRICTION")
        self.play(
            FadeIn(title),
        )
        VGroup(title).arrange(DOWN)
        self.wait(1)
        title_ = TextMobject("FRICTION")
        title_.to_corner(UP + LEFT)
        surface_t = TextMobject("Surface")
        surface = Line(8 * LEFT, 8 * RIGHT)
        surface.shift(2.75 * DOWN)
        surface_t.to_corner(DOWN + LEFT)
        X = np.arange(-8, 8.1, 0.5)
        lines = []
        for x in X:
            lines.append(Line(np.array([x, -2.75, 0]), np.array([x - 0.15, -2.95, 0])))
        self.play(
            LaggedStart(Transform(title, title_),ShowCreation(surface)),
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
            ShowCreation(lines[17]),
            ShowCreation(lines[18]),
            ShowCreation(lines[19]),
            ShowCreation(lines[20]),
            ShowCreation(lines[21]),
            ShowCreation(lines[22]),
            ShowCreation(lines[23]),
            ShowCreation(lines[24]),
            ShowCreation(lines[25]),
            ShowCreation(lines[26]),
            ShowCreation(lines[27]),
            ShowCreation(lines[28]),
            ShowCreation(lines[29]),
            ShowCreation(lines[30]),
            ShowCreation(lines[31]),
            Write(surface_t),
        )

        self.wait()
        