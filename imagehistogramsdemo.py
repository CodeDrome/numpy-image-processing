import imagehistograms as ih


def main():

    print("--------------------------")
    print("| codedrome.com          |")
    print("| NumPy Image Histograms |")
    print("--------------------------\n")
    
    try:

        ih.create_image_histograms('001.jpg')

    except Exception as e:

        print(e)    


if __name__ == "__main__":

    main()
