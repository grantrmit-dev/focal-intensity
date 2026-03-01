"""
Plot intensity cross-sections along X and Y directions.
Converted from plotintensitycrosssectionxy.m
"""
import numpy as np
import matplotlib.pyplot as plt


def plot_intensity_crosssection_xy(X, Y, I, wl, re):
    """
    Plot 1-D cross-sections of the X-Y intensity distribution.

    Parameters
    ----------
    X : 1-D array
        x-axis spatial values (metres).
    Y : 1-D array
        y-axis spatial values (metres).
    I : 2-D array (ny, nx)
        Intensity distribution.
    wl : float
        Wavelength in metres – axis labels are in units of λ.
    re : int
        Number of grid points (used to find the central row/column).
    """
    Imax = I.max()
    if Imax > 0:
        I_norm = I / Imax
    else:
        I_norm = I.copy()

    mid = re // 2

    # Cross-section along X (central row)
    fig_x, ax_x = plt.subplots()
    fig_x.canvas.manager.set_window_title('Intensity along the X-direction')
    Ix = I_norm[mid, :]
    ax_x.plot(X / wl, Ix, 'k')
    ax_x.set_xlabel(r'X($\lambda$)')
    ax_x.set_ylabel('Normalised I (A.U.)')
    ax_x.set_title('Intensity distribution along the X-direction')

    # Cross-section along Y (central column)
    fig_y, ax_y = plt.subplots()
    fig_y.canvas.manager.set_window_title('Intensity along the Y-direction')
    Iy = I_norm[:, mid]
    ax_y.plot(Y / wl, Iy, 'r')
    ax_y.set_xlabel(r'Y($\lambda$)')
    ax_y.set_ylabel('Normalised I (A.U.)')
    ax_y.set_title('Intensity distribution along the Y-direction')

    return fig_x, fig_y
