import cv2

img = cv2.imread('photo.jpg', 0)

cv2.imshow('img', img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
print(img)
