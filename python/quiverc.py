"""
Colour-coded quiver (arrow) plot using the current colourmap.
Converted from quiverc.m (Bertrand Dano, 2003).

Each arrow is coloured according to its magnitude, mapped to the active
matplotlib colourmap (default: 'gray', matching the MATLAB original).
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors


def quiverc(x, y, u, v, scale=1.0, ax=None, colormap='gray', linewidth=1.5,
            alpha_head=0.3, beta_head=0.5):
    """
    Plot colour-coded velocity vectors.

    Parameters
    ----------
    x, y : array-like
        Grid positions (same shape).
    u, v : array-like
        Vector components (same shape as x, y).
    scale : float, optional
        Autoscale multiplier. Set to 0 to disable autoscaling (default 1.0).
    ax : matplotlib.axes.Axes, optional
        Target axes. Uses current axes if None.
    colormap : str, optional
        Matplotlib colourmap (default 'gray').
    linewidth : float, optional
        Arrow line width (default 1.5).
    alpha_head : float, optional
        Arrow head size relative to vector length (default 0.3).
    beta_head : float, optional
        Arrow head base width relative to vector length (default 0.5).

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

    # Broadcast scalar u/v
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

    ax.set_facecolor('white')

    xf = x.ravel()
    yf = y.ravel()
    uf = u.ravel()
    vf = v.ravel()
    mn = mag_norm.ravel()

    eps = np.finfo(float).eps

    for xi, yi, ui, vi, mi in zip(xf, yf, uf, vf, mn):
        color = cmap(mi)
        # Shaft
        ax.plot([xi, xi + ui], [yi, yi + vi],
                color=color, linewidth=linewidth)
        # Arrow head
        hu1 = xi + ui - alpha_head * (ui + beta_head * (vi + eps))
        hu2 = xi + ui - alpha_head * (ui - beta_head * (vi + eps))
        hv1 = yi + vi - alpha_head * (vi - beta_head * (ui + eps))
        hv2 = yi + vi - alpha_head * (vi + beta_head * (ui + eps))
        ax.plot([hu1, xi + ui, hu2], [hv1, yi + vi, hv2],
                color=color, linewidth=linewidth)

    ax.set_facecolor('none')
    ax.tick_params(colors='black')
    for spine in ax.spines.values():
        spine.set_edgecolor('black')

    return ax
