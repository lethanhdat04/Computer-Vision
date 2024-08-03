import cv2

img = cv2.imread('../DATA/00-puppy.jpg')

while True:

    cv2.imshow('Puppy', img)
    
    if cv2.waitKey(0):
        break
        
cv2.destroyAllWindows()