from PIL import Image
import numpy as np


def main():

    print("-----------------")
    print("| codedrome.com |")
    print("| NumPy Image   |")
    print("| Part 1: Intro |")
    print("-----------------\n")
    
    # open Pillow image and create NumPy array from pixel data
    npimage = np.array(Image.open('3x3.png'))

    # print size and color depth
    print("IMAGE INFO\n----------")
    print(f"shape        {npimage.shape}")
    print(f"height       {npimage.shape[0]}")
    print(f"width        {npimage.shape[1]}")
    print(f"colour depth {npimage.shape[2]}")

    # first dimension: rows
    print("\nROWS\n----")
    print(f"1st row\n {npimage[0]}\n")
    print(f"2nd row\n {npimage[1]}\n")
    print(f"3rd row\n {npimage[2]}")

    # second dimension: columns
    print("\nCOLUMNS\n-------")
    print(f"1st column\n {npimage[:,0]}\n")
    print(f"2nd column\n {npimage[:,1]}\n")
    print(f"3rd column\n {npimage[:,2]}")

    # third dimension: color channels
    print("\nCOLOUR CHANNELS\n---------------")
    print(f"RED   \n {npimage[:,:,0]}\n")
    print(f"GREEN \n {npimage[:,:,1]}\n")
    print(f"BLUE  \n {npimage[:,:,2]}\n")

    # create copy of NumPy array
    npimagecopy = np.copy(npimage)

    # multiply green channel by 0.5
    npimagecopy[:,:,1] = npimagecopy[:,:,1] * 0.5

    # set top right pixel to orange
    npimagecopy[0,2] = (255,128,0)

    # create new Pillow image from copy of NumPy array
    imagecopy = Image.fromarray(npimagecopy)
    # and save it
    imagecopy.save("3x3edited.png")


if __name__ == "__main__":

    main()
