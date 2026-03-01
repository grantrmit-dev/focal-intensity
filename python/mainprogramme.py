"""
Main programme for vectorial Debye calculation for a high-NA objective.
Converted from mainprogramme.m

Run this script from the command line:
    python mainprogramme.py

It uses systempra() for default parameters and calls the corresponding
IPSF functions from focal_core.py, then plots the results with matplotlib.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend; change to 'TkAgg' for interactive
import matplotlib.pyplot as plt

from systempra import systempra
from focal_core import compute_intensity


def main():
    sys = systempra()

    print(f"Wavelength is {sys['wl'] * 1e9:.0f} nm.")
    print(f"Numerical-aperture of the objective is {sys['NA']:.1f}.")
    if sys['e'] == 0:
        print("Circular aperture.")
    else:
        print(f"The radius of the annular aperture is {sys['e']:.1f}.")
    if sys['m'] == 0:
        print("Planewave incident beam.")
    else:
        print(f"The topological charge of the phase vortex is {sys['m']:.0f}.")

    # Define coordinate axes
    re = sys['re']
    R = np.linspace(-sys['r'], sys['r'], re)
    Z = np.linspace(-sys['z'], sys['z'], re)
    X = np.linspace(-sys['r'], sys['r'], re)
    Y = np.linspace(-sys['r'], sys['r'], re)

    plane = sys['plane']
    polarization = sys['P']

    if plane == 'X-Y':
        print(f"Calculation of the intensity distribution in the X-Y plane "
              f"at z={sys['z0'] * 1e6:.1f} micron...")
        result = compute_intensity(
            wl=sys['wl'], NA=sys['NA'], n=sys['n'], m=sys['m'],
            e=sys['e'], z0=sys['z0'],
            x_extent=sys['r'], y_extent=sys['r'], z_extent=sys['z'],
            re=re, polarization=polarization, plane='X-Y'
        )
        x_axis = result['x_axis']
        y_axis = result['y_axis']
        I = result['I']
        _plot_xy(sys, x_axis, y_axis, I)

    elif plane == 'R-Z':
        print("Calculation of the intensity distribution in the R-Z plane...")
        result = compute_intensity(
            wl=sys['wl'], NA=sys['NA'], n=sys['n'], m=sys['m'],
            e=sys['e'], z0=sys['z0'],
            x_extent=sys['r'], y_extent=sys['r'], z_extent=sys['z'],
            re=re, polarization=polarization, plane='R-Z'
        )
        r_axis = result['x_axis']
        z_axis = result['y_axis']
        I = result['I']
        _plot_rz(sys, r_axis, z_axis, I)

    else:
        raise ValueError(f"Unknown plane: {plane}. Expected 'X-Y' or 'R-Z'.")

    plt.show()


def _plot_xy(sys, X, Y, I):
    """Plot intensity distribution in the X-Y plane."""
    from plot_intensity_distribution import plot_intensity_distribution
    from plot_intensity_crosssection_xy import plot_intensity_crosssection_xy

    wl = sys['wl']
    re = sys['re']

    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title('Intensity in X-Y plane')
    plot_intensity_distribution(ax, X, Y, I, wl)
    ax.set_xlabel(r'X($\lambda$)')
    ax.set_ylabel(r'Y($\lambda$)')
    ax.set_title('Intensity distribution in the X-Y plane')

    plot_intensity_crosssection_xy(X, Y, I, wl, re)


def _plot_rz(sys, R, Z, I):
    """Plot intensity distribution in the R-Z plane."""
    from plot_intensity_distribution import plot_intensity_distribution
    from plot_intensity_crosssection_rz import plot_intensity_crosssection_rz

    wl = sys['wl']
    re = sys['re']

    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title('Intensity in R-Z plane')
    plot_intensity_distribution(ax, R, Z, I, wl)
    ax.set_xlabel(r'R($\lambda$)')
    ax.set_ylabel(r'Z($\lambda$)')
    ax.set_title('Intensity distribution in the R-Z plane')

    plot_intensity_crosssection_rz(R, Z, I, wl, re)


if __name__ == '__main__':
    main()
