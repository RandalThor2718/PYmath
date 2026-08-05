"""
Mandelbrot Set Renderer in Python
----------------------------------
Renders the Mandelbrot set as a color-mapped image using NumPy for
vectorized computation and Matplotlib for display/saving.
"""

import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(xmin=-2.0, xmax=0.5, ymin=-1.25, ymax=1.25,
               width=800, height=800, max_iter=200):
    """
    Compute the Mandelbrot escape-time values over a grid.

    Returns a 2D array of shape (height, width) where each value is the
    iteration count at which that point escaped (or max_iter if it
    never escaped, i.e. it's considered part of the set).
    """
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    c_re, c_im = np.meshgrid(x, y)
    c = c_re + 1j * c_im

    z = np.zeros_like(c)
    counts = np.zeros(c.shape, dtype=int)
    active = np.ones(c.shape, dtype=bool)

    for i in range(1, max_iter + 1):
        z[active] = z[active] ** 2 + c[active]
        diverged = active & (np.abs(z) > 2)
        counts[diverged] = i
        active[diverged] = False
        if not active.any():
            break

    # Points that never diverged are part of the set
    counts[active] = max_iter

    return counts


def plot_mandelbrot(counts, max_iter=200, cmap="turbo", save_path=None):
    """Display (and optionally save) the Mandelbrot set image."""
    plt.figure(figsize=(8, 8))
    plt.imshow(counts, cmap=cmap, extent=(-2.0, 0.5, -1.25, 1.25),
               interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches="tight", pad_inches=0)
        print(f"Saved to {save_path}")

    plt.show()


if __name__ == "__main__":
    MAX_ITER = 200
    counts = mandelbrot(width=800, height=800, max_iter=MAX_ITER)
    plot_mandelbrot(counts, max_iter=MAX_ITER)

    # To save instead of / in addition to displaying, uncomment:
    # plot_mandelbrot(counts, max_iter=MAX_ITER, save_path="mandelbrot.png")
