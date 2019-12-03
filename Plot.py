import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as mcoll
import matplotlib.colors as mcolors
from matplotlib.widgets import Button
import json as js
from PolygonsSumAndProduct import ButtonCallback


class Scene:
    def __init__(self, points=[], lines=[]):
        self.points = points
        self.lines = lines


class PointsCollection:
    def __init__(self, points=[], **kwargs):
        self.points = points
        self.kwargs = kwargs

    def add_points(self, points):
        self.points = self.points + points


class LinesCollection:
    def __init__(self, lines=[], **kwargs):
        self.lines = lines
        self.kwargs = kwargs

    def add(self, line):
        self.lines.append(line)

    def get_collection(self):
        return mcoll.LineCollection(self.lines, **self.kwargs)


class Plot:
    def __init__(self, scenes=[], json=None):
        if json is None:
            self.scenes = scenes
        else:
            self.scenes = [Scene([PointsCollection(pointsCol) for pointsCol in scene["points"]],
                                 [LinesCollection(linesCol) for linesCol in scene["lines"]])
                           for scene in js.loads(json)]

    def add_scene(self, scene):
        self.scenes.append(scene)

    def add_scenes(self, scenes):
        self.scenes = self.scenes + scenes

    def toJson(self):
        return js.dumps([{"points": [np.array(pointCol.points).tolist() for pointCol in scene.points],
                          "lines": [linesCol.lines for linesCol in scene.lines]}
                         for scene in self.scenes])

    def __configure_buttons(self, callback):
        plt.subplots_adjust(bottom=0.2)
        ax_prev = plt.axes([0.6, 0.05, 0.15, 0.075])
        ax_next = plt.axes([0.76, 0.05, 0.15, 0.075])
        ax_add_point = plt.axes([0.44, 0.05, 0.15, 0.075])
        ax_add_line = plt.axes([0.28, 0.05, 0.15, 0.075])
        b_next = Button(ax_next, 'Następny')
        b_next.on_clicked(callback.next)
        b_prev = Button(ax_prev, 'Poprzedni')
        b_prev.on_clicked(callback.prev)
        b_add_point = Button(ax_add_point, 'Dodaj punkt')
        b_add_point.on_clicked(callback.add_point)
        b_add_line = Button(ax_add_line, 'Dodaj linię')
        b_add_line.on_clicked(callback.add_line)
        return [b_prev, b_next, b_add_point, b_add_line]

    def draw(self):
        plt.close()
        fig = plt.figure()
        callback = ButtonCallback._Button_callback(self.scenes)
        self.widgets = self.__configure_buttons(callback)
        ax = plt.axes()
        callback.set_axes(ax)
        fig.canvas.mpl_connect('button_press_event', callback.on_click)
        plt.show()
        callback.draw()


def test():
    scenes = [Scene([PointsCollection([(1, 2), (3, 1.5), (2, -1)]),
                     PointsCollection([(5, -2), (2, 2), (-2, -1)], color='green', marker="^")],
                    [LinesCollection([[(1, 2), (2, 3)], [(0, 1), (1, 0)]])]),
              Scene([PointsCollection([(1, 2), (3, 1.5), (2, -1)], color='red'),
                     PointsCollection([(5, -2), (2, 2), (-2, 1)], color='black')],
                    [LinesCollection([[(-1, 2), (-2, 3)], [(0, -1), (-1, 0)]])])]

    plot = Plot(scenes)
    plot.add_scene(Scene([PointsCollection([(2, 1)])], [LinesCollection([[(1, 2), (2, 3)]])]))
    plot.draw()


if __name__ == '__main__':
    test()