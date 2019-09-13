from matplotlib import pyplot
import os

def read(filename):
    """ Reads an image with pyplot """
    img = pyplot.imread(filename)
    return img

def save(img):
    """ Saves an image to the output folder. Call BEFORE show """
    filename = createFilename()
    pyplot.imsave(filename, img)
    print('Saved as ' + filename)

def show(img):
    """ Shows an image with pyplot """
    pyplot.imshow(img)
    pyplot.show()

def divider():
    """ Prints a divider """
    print('-----------------------------')

def black_and_whitefy(img):
    for row_index in range(0, len(img)):
        for pixel_index, pixel in enumerate(img[row_index]):
            for rgb_index, rgbval in enumerate(pixel):
                img[row_index][pixel_index][rgb_index] = round(rgbval)
    return img

def rgbImage2grayVector(img):
    """ Turns a row and column rgb image into a 1D grayscale vector """
    gray = []
    for row_index in range(0, len(img)):
        for pixel_index, pixel in enumerate(img[row_index]):
            gray.append(rgbPixel2grayscaleValue(pixel))

    return gray

def rgbPixel2grayscaleValue(rgb):
    r, g, b = rgb[0], rgb[1], rgb[2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

def createFilename():
    """
    Returns an unused name for an output
    """
    for i in range(0, 1000):
        if (i<10):
            filename = 'output/output_00' + str(i) + '.png'
        elif (i<100):
            filename = 'output/output_0' + str(i) + '.png'
        else:
            filename = 'output/output_' + str(i) + '.png'

        if (not os.path.exists(filename)):
            return filename
            # file = open(filename, 'w+')
            # file.close()



filename    = 'Resources/homer.png'
# filename    = 'Resources/qiskit.png'

img         = read(filename)

gray        = rgb2gray(img)

# print(gray)

save(img)
# show(img)



