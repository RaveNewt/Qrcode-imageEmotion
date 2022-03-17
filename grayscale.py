#packages
import cv2
#Open Image file
img = cv2.imread("test.jpg", cv2.IMREAD_UNCHANGED)
#convert image to grayscale
img_grayscale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#convert to black image
thresh, img_black = cv2.threshold(img_grayscale, 180, 200, cv2.THRESH_BINARY)
#show image
#cv2.imshow("Image.jpg", img)
#cv2.imshow("Image.jpg", img_grayscale) #grayscale
cv2.imshow("Image.jpg", img_black) #black
#break out of key press
cv2.waitKey(0)
#clean up windows
cv2.destroyAllWindows()
