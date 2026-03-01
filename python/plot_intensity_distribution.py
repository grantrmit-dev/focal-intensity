"""
Plot intensity distribution as a 2D heatmap.
Converted from plotintensitydistribution.m
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from scipy.ndimage import zoom


def plot_intensity_distribution(ax, X, Y, I, wl, colormap='jet'):
    """
    Display a normalised 2D intensity heatmap.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes to draw into.
    X : 1-D array
        Spatial x-axis values (metres).
    Y : 1-D array
        Spatial y-axis values (metres).
    I : 2-D array (ny, nx)
        Intensity values.
    wl : float
        Wavelength in metres – used to normalise axis labels to units of λ.
    colormap : str, optional
        Matplotlib colourmap name (default 'jet').
    """
    Imax = I.max()
    if Imax > 0:
        I_norm = I / Imax
    else:
        I_norm = I

    # Upsample to 1080×1080 (equivalent to MATLAB imresize)
    scale_y = 1080 / I_norm.shape[0]
    scale_x = 1080 / I_norm.shape[1]
    Id = zoom(I_norm, (scale_y, scale_x), order=1)

    x_lam = X / wl
    y_lam = Y / wl
    extent = [x_lam[0], x_lam[-1], y_lam[0], y_lam[-1]]

    im = ax.imshow(
        Id,
        extent=extent,
        origin='lower',
        aspect='equal',
        cmap=colormap,
        norm=Normalize(vmin=0, vmax=1),
    )
    plt.colorbar(im, ax=ax)
    ax.set_xlabel(r'X($\lambda$)')
    ax.set_ylabel(r'Y($\lambda$)')
    return im
