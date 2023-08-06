from LSBSteg_Script_To_Student import *


# decoding
im = cv2.imread("my_new_imageW.png")
steg = LSBSteg(im)
print("Text value:",steg.decode_text())
