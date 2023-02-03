import cv2
cv2.imread("solar-systm.jpg")
cv2.imshow("output",img)
cv2.waitKey

cv2.putText(img,
            "sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
