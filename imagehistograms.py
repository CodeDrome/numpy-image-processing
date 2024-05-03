from PIL import Image
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def create_image_histograms(filename):

    '''
    The single "public" function in the module
    which attempts to create a set of 3 colour
    histograms for the image file specified
    by the filename argument.
    Exceptions caused by file errors are raised to
    the calling code which therefore should include
    exception handling.    
    '''

    try:

        # get a NumPy array of pixel data
        # (this will be 3 2-dimensional arrays)
        npimage = np.array(Image.open(filename))

        # get a tuple of 1-dimensional arrays for R, G & B
        npimage_2d = _as_2d(npimage)

        # get a tuple of frequencies of values 0 to 255
        # for R, G & B
        counts = _get_rgb_frequencies(npimage_2d)

        # pass the above tuple to _histograms to 
        # plot the data
        _histograms(counts, filename)

    except Exception as e:

        raise e
    

def _as_2d(npimage):

    # separate out the 3 colour channels
    r, g, b = np.split(npimage, 3, 2)

    pixelcount = r.size
    
    # change to 1-dimensional
    r = np.reshape(r, pixelcount)
    g = np.reshape(g, pixelcount)
    b = np.reshape(b, pixelcount)

    return (r, g, b)


def _get_rgb_frequencies(npimage_2d):

    # get frequencies for each colour
    red_counts = np.bincount(npimage_2d[0], minlength=256)
    green_counts = np.bincount(npimage_2d[1], minlength=256)
    blue_counts = np.bincount(npimage_2d[2], minlength=256)

    # get the highest frequency for each colour . . .
    max_red = np.max(red_counts)
    max_green = np.max(green_counts)
    max_blue = np.max(blue_counts)

    # . . . and then the highest frequency for all colours
    max_count = max(int(max_red), int(max_green), int(max_blue))

    # normalise the data to a value between 0 and 1
    red_counts = red_counts / max_count
    green_counts = green_counts / max_count
    blue_counts = blue_counts / max_count

    return (red_counts, green_counts, blue_counts)
    

def _histograms(counts, filename):

    # all three histograms are plotted from 
    # 0 to 255 on the x axis
    # and
    # 0 to 1 on the y axis.
    # These are used below 
    xlim = [0.0, 255.0]
    ylim = [0.0, 1.0]

    # This is used later to force Matplotlib to
    # include all values in the range even if
    # there is no data for some of them.
    possible_values = np.arange(0,256)

    # the rest is standard Matplotlib code to create the histograms
    fig, axs = plt.subplots(nrows=3, ncols=1, sharey=False)
    
    plt.get_current_fig_manager().set_window_title(f"Image File: {filename}")

    fig.tight_layout()

    # Should I have used a loop from 0 to 2 here?
    # Or would that be an over-complication?
    # Can't decide . ¯\_(ツ)_/¯
    axs[0].set_xlim(xlim[0], xlim[1])
    axs[0].set_ylim(ylim[0], ylim[1])
    
    axs[1].set_xlim(xlim[0], xlim[1])
    axs[1].set_ylim(ylim[0], ylim[1])
    
    axs[2].set_xlim(xlim[0], xlim[1])
    axs[2].set_ylim(ylim[0], ylim[1])

    axs[0].hist(possible_values, weights=counts[0], bins=256, color='#FF0000')
    axs[1].hist(possible_values, weights=counts[1], bins=256, color='#00FF00')
    axs[2].hist(possible_values, weights=counts[2], bins=256, color='#0000FF')

    plt.show()
