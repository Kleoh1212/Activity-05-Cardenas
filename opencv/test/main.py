import cv2
import numpy

def main():
    print("""
       ACTIVITY #5:
       The program should be:
       1. Accept/load colored img. Grayscale should be rejected.
       2. Output a pixel value.
       3. Modify a pixel value.
       4. Set img dimensions. Within boundaries or not.
       5. Set img total pixel count. Higher or lower than the set pixel.
       6. Show the currently loaded image's data type.
       0. Close Window
       """)

    opt = int(input("Select Action: "))
  
    if opt == 1:
        Grayscale()    
    elif opt == 2:
       PixelVal() 
    elif opt == 3:
        ModifyPV()
    elif opt == 4:
        imgDim()
    elif opt == 5:
        PixelCount()
    elif opt == 6:
        ImgDataType()
    elif opt == 0:
        exit()
    else:
        print("Please try again.")
        main()   

    def Grayscale():
        img = cv2.imread('1.jpg')
        print("Accept/load colored img. Grayscale should be rejected.")
        imgLen = len(img.shape)
        if imgLen >= 3:
            cv2.imshow("colored")
            cv2.waitKey(0)
            main()
        else:
            print("Grayscale")
            main()
    def PixelVal():
        img = cv2.imread('1.jpg')
        print("Output a pixel value.")
        x = int(input("for X axis: "))
        y = int(input("for Y axis: "))
        color = int(input("BGR selection: [BLUE] [GREEN] [RED]: "))
        print(img.item(x, y, color))
        cv2.waitKey(0)
        main()

    def ModifyPV():
        img = cv2.imread('1.jpg')
        print(" Modify a pixel value.")
        x = int(input("for x axis: "))
        y = int(input("for y axis: "))
        print(img[x, y])
        for i in range(0, 3, 1):
            if i == 0:
                print("Please Enter value for blue")
                pixelValue = int(input("Pixel Value: "))
            elif i == 1:
                print("Please Enter value for green")
                pixelValue = int(input("Pixel Value: "))
            elif i == 2:
                print("Please Enter value for red")
                pixelValue = int(input("Pixel Value: "))
        
            img.itemset((x, y, i), pixelValue)
        print(img[x, y])
        cv2.imshow("Colored",img)
        cv2.waitKey(0)
        main()  
    def imgDim():
        img = cv2.imread('1.jpg')
        print(" Set img dimensions. Within boundaries or not.")
        x = 300
        y = 250
        print(img.shape)
        print(f"""
        Total Pixel in X-axis: {img.shape[0]}
        Total Pixel in Y-axis: {img.shape[1]}
        Compared Value in X-axis: {x}
        Compared Value in Y-axis: {y}
        """)
        if x <= img.shape[0] and y <= img.shape[1]:
            print("Within boundaries")
        else:
            print("Out of boundaries")
        cv2.waitKey(0)
        main()

    def PixelCount():
        img = cv2.imread('1.jpg')
        print(" Set img total pixel count. Higher or lower than the set pixel.")
        x = 300
        y = 250
        fixedValue = x * y
        totalPixel = img.shape[0] * img.shape[1]
        print("""
        Total Fixed Variable: {fixedValue}
        Total Image Pixels: {totalPixel}
        """)
        if fixedValue > totalPixel:
            print("HIGHER")
        elif fixedValue < totalPixel:
            print("LOWER")
        else:
            print("EQUA:L")
        main()
    def ImgDataType():
        img = cv2.imread('1.jpg')
        print("Show the currently loaded image's data type.")
        print("Image data type is: {img.dtype}")
        main()
if __name__  == ("__main__"):
    main()