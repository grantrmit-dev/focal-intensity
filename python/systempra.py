"""
System parameters for the vectorial Debye focal field calculation.
Converted from systempra.m
"""


def systempra():
    """Return default system parameters as a dictionary."""
    return {
        'wl':    800e-9,    # Free-space wavelength (m)
        're':    210,       # Resolution (pixels per side)
        'r':     1e-6,      # XY calculation half-width (m)
        'z':     1e-6,      # Z calculation half-width (m)
        'z0':    0.0,       # Image plane axial position (m)
        'NA':    1.4,       # Numerical aperture
        'n':     1.514,     # Refractive index  (oil=1.514, water=1.33, air=1.0)
        'P':     'Circular',# Polarisation: 'Linear'|'Circular'|'Radial'|'Azimuthal'
        'e':     0.0,       # Normalised inner radius of annular aperture (0=full)
        'm':     0,         # Topological charge (0=plane wave)
        'plane': 'R-Z',     # Calculation plane: 'X-Y'|'R-Z'
    }
