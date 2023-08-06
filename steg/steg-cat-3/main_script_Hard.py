from LSBSteg_Script_To_Student import *


#decoding binary
steg = LSBSteg(cv2.imread("new_image_binary.png"))
binary_data = steg.decode_binary()
with open("recovered_data.bin", "w+b") as image_bin:
    image_bin.write(binary_data)
