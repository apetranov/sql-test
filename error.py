import cv2
import numpy

cv2.namedWindow("error_window", cv2.WINDOW_NORMAL)


image = cv2.imread("images/cat.jpg")

top_text = input("Top text: ")
bottom_text = input("Bottom text: ")

cv2.putText(
    image, 
    top_text, 
    (200, 100), 
    cv2.FONT_HERSHEY_SIMPLEX, 
    2,
    (0, 0, 0),
    9
    )

cv2.putText(
    image, 
    top_text, 
    (200, 100), 
    cv2.FONT_HERSHEY_SIMPLEX, 
    2,
    (255, 255, 255),
    5
    )


cv2.putText(
    image, 
    bottom_text, 
    (150, 550), 
    cv2.FONT_HERSHEY_SIMPLEX, 
    1,
    (0, 0, 0),
    6
    )


cv2.putText(
    image, 
    bottom_text, 
    (150, 550), 
    cv2.FONT_HERSHEY_SIMPLEX, 
    1,
    (255, 255, 255),
    2
    )


# cv2.imshow("error_window", image)
# cv2.waitKey(0)

output_filename = "error3.jpg"
cv2.imwrite(output_filename, image)
