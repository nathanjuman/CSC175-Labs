#----------------------------------------------------------------------------------------------------------------------------------------
#This program processes an image for the total number of pixels in an image file, and finds the number of pixels for several conditions. 
#Nathan Juman, CSC-175-01
#----------------------------------------------------------------------------------------------------------------------------------------
import image

def totalPixels(img) :
    '''
    This function calculates the total amount of pixels in a given image.

    Parameters:
    img : Given image to have the total pixels calculated

    Return :
    tp (int) : Total amount of pixels in the image file
    '''
   
    w = img.getWidth()
    h = img.getHeight()
    tp = w * h
    return tp

def redLargestPixel(r, g, b) :
    '''
    This function takes a pixel and returns True if red is the rgb color with the highest intensity, and False if red is not the rgb color with the highest intensity.

    Parameters:
    r, g, b (int) : red, green, and blue values for a pixel

    Returns:
    (bool) : True if red has the highest intensity, False if not
    '''
    if r > g and r > b :
        return True
    else:
        return False

def greenLargestPixel(r, g, b) :
    '''
    This function takes a pixel and returns True if green is the rgb color with the highest intensity, and False if green is not the rgb color with the highest intensity.

    Parameters:
    r, g, b (int) : red, green, and blue values for a pixel

    Returns:
    (bool) : True if green has the highest intensity, False if not
    '''
    if g > r and g > b :
        return True
    else :
        return False

def blueLargestPixel(r, g, b) :
    '''
    This function takes a pixel and returns True if blue is the rgb color with the highest intensity, and False if blue is not the rgb color with the highest intensity.

    Parameters:
    r, g, b (int) : red, green, and blue values for a pixel

    Returns:
    (bool) : True if blue has the highest intensity, False if not
    '''
    if b > r and b > g :
        return True
    else :
        return False

def highestIntensityCount(img):
    '''
    This function goes through each pixel and uses previous functions to decide what the most dominant color is.

    Parameters:
    img: Image given where each pixel is calculated.

    Return:
    (int) Each color has the amount have pixels where it is most dominant, as well as the pixel where no color is the most dominant. 
    '''
    w = img.getWidth()
    h = img.getHeight()

    redAmount = 0
    greenAmount = 0
    blueAmount = 0
    same = 0

    for row in range(h) :
        for col in range(w) :
            p = img.getPixel(col, row)
            r = p.getRed()
            g = p.getGreen()
            b = p.getBlue()

            if redLargestPixel(r, g, b) == True :
                redAmount += 1
            elif greenLargestPixel(r, g, b) == True :
                greenAmount += 1
            elif blueLargestPixel(r, g, b) == True :
                blueAmount += 1
            else :
                same += 1

    return redAmount, greenAmount, blueAmount, same


def main() :
    img = image.Image("lab6_castle.gif")
    
    print("Total Amount of Pixels:", totalPixels(img))
    print("")
    print("Amount of Pixels with Highest Intensity: ")
    print(" Red  Green  Blue  None ")
    print(highestIntensityCount(img))

main()
