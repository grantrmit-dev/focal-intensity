"""
Test script: load a text array and display it as a coloured image.
Converted from test_load.m
"""
import numpy as np
import matplotlib.pyplot as plt

from extract_colormap import extract_colormap


def main():
    A = np.loadtxt('test.txt')

    mycolor = extract_colormap(level=1024)

    # Build a ListedColormap from the (1024, 3) float array
    from matplotlib.colors import ListedColormap
    cmap = ListedColormap(mycolor)

    fig, ax = plt.subplots()
    im = ax.imshow(A, cmap=cmap, origin='upper', aspect='auto')
    plt.colorbar(im, ax=ax)
    ax.set_title('test.txt – custom colourmap')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
