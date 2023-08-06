# Installation
Conda\
opencv, numpy, docopt using conda\
Github https://github.com/RobinDavid/LSB-Steganography\


### To make sure the challenges work correctly the image must larger than text_length*8
### The sutdents will receive a LSBSteg_decode.py script as a starting point to solve the challenges

# Easy challenge: changing the code to use the second LSB or third LSB
Solution: To solve the challenge, the students must understand the provided LSBSteg.py
1. The students go to the decode_text(), add a new parameter, which allows the students to choose which LSB to decode the message
2. The students add a new line to assign the parameter to the self.maskONE variable to apply the chosen LSB in the decoding process
3. The students start to try each LSB until they choose the correct one

# Medium challenge: changing the code to alternate the LSB choice based on bit's order in an 8 bit array to get the hidden image
Solution: To solve the challenge, the students must understand the provided LSBSteg.py in a deeper level
1. The students go to read_bit(), add a new parameter, which allows the function to receive different LSB during the decoding process
2. The students change the variable self.maskONE to the new created parameter in read_bit() to apply the chosen LSB
3. The students go to read_bits(), add a condition to check whether the bit's order is odd or even in an octa or an 8 bit array, and apply the corresponding LSB to each scenario

# Hard challenge: recognising the file's header and using hex editor to reconstruct the file's header
Solution: To solve the challenge, the students must use the medium challenge solution, understand the file's header, and know how to use hex editor to reconstruct the file's header
1. The students apply the same Medium challenge's solution to extract the payload hidden in the image
2. The students read the payload using a hex editor, navigate the header, identify the file's type based on the header. and change the file's extension to read the payload properly
3. As the payload is a zip, the student can extract the content inside, the content is a corrupted image
4. The students use a hex editor to read the corrupted image, correct the header structure and open the image to get answer


# Tutorial main points should be covered but not limit to
## Easy challenge
+ Teach the students about the LSBSteg.py code
+ Guide the students through the important code lines and variables
## Medium challenge
+ Guide the students to note about the deeper functions which are used to change the bits
+ Adjustment happens in read_bits() and read_bit()
+ Hint the students about using condition and loop
## Hard challenge
+ Teach the students about file's header and hex editor
+ There is no adjustment to the code, as the students must resue the work in Medium challenge
+ The hard challenge is at the part where the students need to identify the file type, change file extension, and resconstruct header
+ List of file headers: https://en.wikipedia.org/wiki/List_of_file_signatures
+ Hex editor online: https://hexed.it/
## Practice challenge
+ The provided LSBSteg script to the student has errors and typos
+ Based on the presentation and the guidance, the students correct all the bugs and can run the script normally to get the hidden message
+ The practice main's aim is helping the students to understand the technique mechanism and the code

# Notes
The maskONE and maskZERO are used to choose which bit to change\
put_binary_value() is used to hide text message in an image\
read_bit() is the most important method to get the message out using the maskONE\
mention that in the alternate LSB numbers challenges, the length of the payload are encoded the same way as the payload's content\
Easy challenge:
+ Encoder and solution in LSBSteg_Easy.py\
Medium challenge:
+ Encoder and solution in LSBSteg\_Medium_Hard.py\
Hard challenge:
+ Encoder and solution in LSBSteg_Medium_Hard.py
