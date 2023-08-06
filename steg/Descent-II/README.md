# Descent II

## Flag

`pecan{4nd_d0wn_w3_g0}`

## Info

A file has been hidden inside this image containing a flag.

### Hint

What tool does Kali use to hide data in images?

## Solution

1. `steghide --extract -sf descent2.jpg -xf flag.txt`
2. The flag is in the file