"""
Custom colormap loader.
Converted from ExtractColormap.m

Original MATLAB reads a PNG strip 'colorbar2.png' and resamples it.
The Python version provides the same interface but falls back to
matplotlib's 'jet' colormap when the PNG is unavailable.
"""
import numpy as np
import os


def extract_colormap(level=256, png_path=None):
    """
    Return an (level x 3) float array of RGB values in [0, 1].

    Parameters
    ----------
    level    : int  - number of colormap entries
    png_path : str  - path to colorbar2.png (optional)

    Returns
    -------
    cmap : ndarray, shape (level, 3), dtype float64
    """
    if png_path is None:
        # Try sibling directory
        here = os.path.dirname(os.path.abspath(__file__))
        candidate = os.path.join(here, '..', 'colorbar2.png')
        if os.path.isfile(candidate):
            png_path = candidate

    if png_path and os.path.isfile(png_path):
        try:
            from PIL import Image
            img = np.array(Image.open(png_path).convert('RGB'))
            img = img[::-1]               # flipud
            # Take the first column and resize to `level` entries
            col = img[:, 0, :]            # shape (H, 3)
            H = col.shape[0]
            idx = np.round(np.linspace(0, H - 1, level)).astype(int)
            cmap = col[idx].astype(np.float64) / 255.0
            return cmap
        except ImportError:
            pass  # Pillow not available, fall through

    # Fallback: use matplotlib jet
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    cmap_obj = plt.get_cmap('jet', level)
    return cmap_obj(np.linspace(0, 1, level))[:, :3]
