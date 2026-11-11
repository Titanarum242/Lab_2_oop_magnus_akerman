import numpy as np
from sphere import Sphere
from space_3d import Translate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Plot3D:

    def __init__(self):
        self._objects = []

    def add_sphere(self, sphere, color="r"):

        if not isinstance(sphere, Sphere):
            raise TypeError(
                f"Expected Sphere, got {type(sphere).__name__}"
            )

        self._objects.append((sphere, color))

    def plot(self):

        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection="3d")

        for sphere, color in self._objects:

            x0 = sphere._translate.x
            y0 = sphere._translate.y
            z0 = sphere._translate.z
            r = sphere._radius

            u = np.linspace(0, 2 * np.pi, 40)
            v = np.linspace(0, np.pi, 40)

            x = x0 + r * np.outer(np.cos(u), np.sin(v))
            y = y0 + r * np.outer(np.sin(u), np.sin(v))
            z = z0 + r * np.outer(np.ones_like(u), np.cos(v))

            ax.plot_surface(x, y, z, color=color, alpha=0.3,linewidth=0)

            ax.scatter(x0, y0, z0, color="black", s=30)
           
        
        max_radius = max(sphere._radius for sphere, _ in self._objects)
        ax.set_xlim(-10 - max_radius, 10 + max_radius)
        ax.set_ylim(-10 - max_radius, 10 + max_radius)
        ax.set_zlim(-10 - max_radius, 10 + max_radius)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        ax.set_box_aspect([1, 1, 1])

        plt.show()

if __name__ == "__main__":
    plotter = Plot3D()
    plotter.add_sphere(Sphere(2, Translate(0, 0, 0)), color="r")
    plotter.add_sphere(Sphere(1, Translate(3, 3, 3)), color="g")
    plotter.add_sphere(Sphere(1.5, Translate(-3, -3, -3)), color="b")
    plotter.plot()