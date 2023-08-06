from LSBSteg_Script_To_Student import *


#decoding image
steg = LSBSteg(cv2.imread("new_cat_image.png"))
orig_im = steg.decode_image()
cv2.imwrite("recovered.png", orig_im)
