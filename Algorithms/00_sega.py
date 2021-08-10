import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="157.jpg",
	help="path to the input image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])

# Inicial Location
y2=550      # y2 maximum height
x2=340      # x2 maximum width
yy=2        # Step y


############
y1=y2-150   # y1 minimum height
x1=x2-100   # x1 minimum width
xx=30       # Step x
maxi=20     # number of results


ins=0
for i in range(0,maxi):
    print(i)
    ins = image[(y1+(i*yy)):y2+(i*yy), x1+(i*xx):x2+(i*xx)]
    cv2.imshow("Insulator", ins)
    cv2.waitKey(500)
    cv2.imwrite('I157_%02i.jpg' %i, ins)
cv2.destroyAllWindows()


'''
# Draw rectangle
img2 = cv2.rectangle(image,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imshow("Original", img2)
cv2.waitKey(2000)
cv2.destroyAllWindows()
'''


'''
ins=0
for i in range(0,maxi):
    print(i)
    #ins = image[(y1+(i*yy)):y2+(i*yy), x1+(i*xx):x2+(i*xx)]
    ins = cv2.rectangle(image,(x1+(i*xx),y1+(i*yy)),(x2+(i*xx),y2+(i*yy)),(10*i,0,250-10*i),2)
    cv2.imshow("Insulator", ins)
    cv2.waitKey(0)
    cv2.imwrite('I50_%02i.jpg' %i, ins)
cv2.destroyAllWindows()
'''

    
       

