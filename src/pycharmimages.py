import cv2
from datetime import datetime

# # read an image
# img = cv2.imread('lena.jpg', 1)  # 0 means grayscale, 1 means color, -1 is untouched
# print(img)
#
# # display image
# image_name = 'image'
# cv2.imshow(image_name, img)
#
# # keep image showing
# k = cv2.waitKey(0)
#
# if k == 27:
#     # destroy all windows created
#     cv2.destroyAllWindows()
# elif k == ord('s'):
#     # save the image to a second image
#     # write an image
#     cv2.imwrite('lena_copy.png', img)


def display_image(image_url, scale, img_name, seconds):
    # read the image
    img = cv2.imread(image_url, scale)

    if img_name is None:
        current_time = datetime.now()
        img_name = "Image" + str(current_time)

    cv2.imshow(img_name, img)

    # keep image showing for time in 'seconds'
    millsec_to_sec = 1000
    real_time = seconds * millsec_to_sec

    cv2.waitKey(real_time)


display_image('lena.jpg', 1, 'Hat Lady', 5)

