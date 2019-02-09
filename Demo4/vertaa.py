import cv2
import matplotlib
matplotlib.use('Agg') #jotta ei kayta nayttoa
import matplotlib.pyplot as plt


img1 = cv2.imread("hiiri1.jpg")
img2 = cv2.imread("hiiri2.jpg")


# ORB dtector

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Brute force matching


bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

matching_result = cv2.drawMatches(img1, kp1, img2, kp2, matches, None, flags=2)


plt.imshow(cv2.cvtColor(matching_result,cv2.COLOR_BGR2RGB)), plt.savefig("tulos.png")





