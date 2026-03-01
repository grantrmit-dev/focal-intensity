"""
Colour-coded quiver plot – compact variant (no arrow heads).
Converted from quiverc2.m (Bertrand Dano, 2003).

Differences from quiverc.py:
  - Default autoscale = 0.65 (vs 1.0 in quiverc)
  - Arrow heads are commented out in the original; only shafts are drawn.
  - Background is black with white axes (matching the MATLAB original).
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def quiverc2(x, y, u, v, scale=0.65, ax=None, colormap='jet', linewidth=1.5):
    """
    Plot colour-coded velocity vector shafts (no arrow heads).

    Parameters
    ----------
    x, y : array-like
        Grid positions (same shape).
    u, v : array-like
        Vector components (same shape as x, y).
    scale : float, optional
        Autoscale multiplier (default 0.65; set to 0 to disable).
    ax : matplotlib.axes.Axes, optional
        Target axes. Uses current axes if None.
    colormap : str, optional
        Matplotlib colourmap (default 'jet').
    linewidth : float, optional
        Line width (default 1.5).

    Returns
    -------
    ax : matplotlib.axes.Axes
    """
    if ax is None:
        ax = plt.gca()

    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    u = np.asarray(u, dtype=float)
    v = np.asarray(v, dtype=float)

    if u.size == 1:
        u = np.full_like(x, u.flat[0])
    if v.size == 1:
        v = np.full_like(u, v.flat[0])

    # Autoscale
    if scale != 0:
        if x.ndim == 1:
            n = m = int(np.sqrt(x.size))
        else:
            m, n = x.shape
        delx = (x.max() - x.min()) / max(n, 1)
        dely = (y.max() - y.min()) / max(m, 1)
        denom = delx ** 2 + dely ** 2
        if denom > 0:
            length = np.sqrt((u ** 2 + v ** 2) / denom)
            max_len = length.max()
            if max_len > 0:
                autoscale = scale * 0.9 / max_len
                u = u * autoscale
                v = v * autoscale

    # Colour by magnitude
    mag = np.sqrt(u ** 2 + v ** 2)
    mag_max = mag.max()
    if mag_max > 0:
        mag_norm = mag / mag_max
    else:
        mag_norm = np.zeros_like(mag)

    cmap = cm.get_cmap(colormap, 64)

    # Black background, white axes (matches MATLAB quiverc2)
    ax.set_facecolor('black')
    ax.tick_params(colors='white')
    for spine in ax.spines.values():
        spine.set_edgecolor('white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    if ax.figure:
        ax.figure.patch.set_facecolor('black')

    xf = x.ravel()
    yf = y.ravel()
    uf = u.ravel()
    vf = v.ravel()
    mn = mag_norm.ravel()

    for xi, yi, ui, vi, mi in zip(xf, yf, uf, vf, mn):
        color = cmap(mi)
        ax.plot([xi, xi + ui], [yi, yi + vi],
                color=color, linewidth=linewidth)

    return ax
