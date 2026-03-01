"""
Plot intensity cross-sections along R and Z directions.
Converted from plotintensitycrosssectionrz.m
"""
import numpy as np
import matplotlib.pyplot as plt


def plot_intensity_crosssection_rz(R, Z, I, wl, re):
    """
    Plot 1-D cross-sections of the R-Z intensity distribution.

    Parameters
    ----------
    R : 1-D array
        Radial axis spatial values (metres).
    Z : 1-D array
        Axial axis spatial values (metres).
    I : 2-D array (nz, nr)
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

    # Cross-section along R (central row)
    fig_r, ax_r = plt.subplots()
    fig_r.canvas.manager.set_window_title('Intensity along the R-direction')
    Ir = I_norm[mid, :]
    ax_r.plot(R / wl, Ir, 'k')
    ax_r.set_xlabel(r'R($\lambda$)')
    ax_r.set_ylabel('Normalised I (A.U.)')
    ax_r.set_title('Intensity distribution along the R-direction')

    # Cross-section along Z (central column)
    fig_z, ax_z = plt.subplots()
    fig_z.canvas.manager.set_window_title('Intensity along the Z-direction')
    Iz = I_norm[:, mid]
    ax_z.plot(Z / wl, Iz, 'r')
    ax_z.set_xlabel(r'Z($\lambda$)')
    ax_z.set_ylabel('Normalised I (A.U.)')
    ax_z.set_title('Intensity distribution along the Z-direction')

    return fig_r, fig_z
