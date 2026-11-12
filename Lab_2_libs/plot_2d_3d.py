import numpy as np
from sphere import Sphere
from cube import Cube
from circle import Circle
from rectangle import Rectangle
from space_3d import Translate
import matplotlib.pyplot as plt
from itertools import combinations

class Plt2d:
    """ 
    Got help from co-pilot to write this class.

    A class for plotting 2D shapes using Matplotlib. """

    def __init__(self):
        self._objects = []

    def add(self, shape, color="b"):
        self._objects.append((shape, color))

    def plot(self):

        fig, ax = plt.subplots()

        for shape, color in self._objects:

            if isinstance(shape, Circle):

                patch = plt.Circle((shape.circle_center[0], shape.circle_center[1]), shape._radius, color=color, fill=False)

                ax.plot(shape.circle_center[0], shape.circle_center[1], 'o', color='black')

                ax.add_patch(patch)

            elif isinstance(shape, Rectangle):

                x0 = shape._translate._x
                y0 = shape._translate._y
                w = shape._base
                h = shape._height

                rect = plt.Rectangle(
                    (x0, y0), w, h, color=color, fill=False) 
                
                ax.plot(x0 + w/2, y0 + h/2, 'o', color='black')

                ax.add_patch(rect)

        """ to set scaling of the axis in the diagram the maximum radius or side is used among the shape values"""

        max_radius = max((c._radius for c, _ in self._objects if isinstance(c, Circle)), default=0)

        max_base_height = max((max(r._base, r._height) for r, _ in self._objects if isinstance(r, Rectangle)), default=0)

        max_size = max(max_radius, max_base_height)

        ax.set_xlim(-10 - max_size, 10 + max_size)
        ax.set_ylim(-10 - max_size, 10 + max_size)
        ax.set_aspect('equal')

        plt.show()

if __name__ == "__main__":
    c1 = Circle(5, Translate(0, 0))
    c2 = Circle(3, Translate(5, 5))

    r1 = Rectangle(4, 6, Translate(-5, -5))
    r2 = Rectangle(2, 8, Translate(-10, 10))

    plot = Plt2d()

    plot.add(c1, "red")
    plot.add(c2, "blue")
    plot.add(r1, "green")
    plot.add(r2, "orange")

    plot.plot()




class Plt3d:
    """
    *got help from co-pilot to write this class*

    A class for plotting 3D shapes (spheres and cubes) using Matplotlib.
    """

    def __init__(self):
        self._objects = []

    def add(self, shape, color="b"):
        self._objects.append((shape, color))

    def _plot_sphere(self, ax, sphere, color):

        x0 = sphere._translate._x
        y0 = sphere._translate._y
        z0 = sphere._translate._z
        r = sphere._radius

        u = np.linspace(0, 2 * np.pi, 40)
        v = np.linspace(0, np.pi, 40)

        x = x0 + r * np.outer(np.cos(u), np.sin(v))
        y = y0 + r * np.outer(np.sin(u), np.sin(v))
        z = z0 + r * np.outer(np.ones_like(u), np.cos(v))

        ax.plot_surface(x, y, z, color=color, alpha=0.3, linewidth=0)

        ax.scatter(x0, y0, z0, color="black", s=30)

    def _plot_cube(self, ax, cube, color):

        x0 = cube._translate._x
        y0 = cube._translate._y
        z0 = cube._translate._z

        L = cube._side_length

        vertices = np.array([
            [x0,     y0,     z0],
            [x0+L,   y0,     z0],
            [x0+L,   y0+L,   z0],
            [x0,     y0+L,   z0],
            [x0,     y0,     z0+L],
            [x0+L,   y0,     z0+L],
            [x0+L,   y0+L,   z0+L],
            [x0,     y0+L,   z0+L]
        ])

        for start, end in combinations(vertices, 2):

            diff = np.abs(start - end)

            if np.count_nonzero(diff) == 1:
                ax.plot3D(*zip(start, end), color=color,linewidth=2)

        ax.scatter(
            x0 + L/2,
            y0 + L/2,
            z0 + L/2,
            color="black",
            s=30
        )

    def plot(self):

        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection="3d")

        mins = []
        maxs = []

        for shape, color in self._objects:

            if isinstance(shape, Sphere):

                self._plot_sphere(ax, shape, color)

                r = shape._radius
                x = shape._translate._x
                y = shape._translate._y
                z = shape._translate._z

                mins.extend([x-r, y-r, z-r])
                maxs.extend([x+r, y+r, z+r])

            elif isinstance(shape, Cube):

                self._plot_cube(ax, shape, color)

                L = shape._side_length
                x = shape._translate._x
                y = shape._translate._y
                z = shape._translate._z

                mins.extend([x, y, z])
                maxs.extend([x+L, y+L, z+L])

        if mins and maxs:

            min_val = min(mins)
            max_val = max(maxs)

            ax.set_xlim(min_val, max_val)
            ax.set_ylim(min_val, max_val)
            ax.set_zlim(min_val, max_val)

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_box_aspect([1, 1, 1])

        plt.show()


if __name__ == "__main__":
    sp1 = Sphere(5, Translate(-11, 1, 8))
    sp2 = Sphere(8, Translate(15, 0, 5))

    cb1 = Cube(10, Translate(20, 20, 0))

    plotter = Plt3d()

    plotter.add(sp1, "red")
    plotter.add(sp2, "blue")
    plotter.add(cb1, "green")

    plotter.plot()





