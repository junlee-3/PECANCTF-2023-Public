# Descent I

## Flag

`pecan{th3_d3sc3nt_b3g1ns}`

## Info

Something about the image file has been changed to hide a message.

### Hint

Have you heard of EXIF?


## Solution

Find an EXIF viewer online or use `exiftool`. The flag should be in base64 as the description of the image.

Image description: cGVjYW57dGgzX2Qzc2MzbnRfYjNnMW5zfQo=
Flag: `pecan{th3_d3sc3nt_b3g1ns}`