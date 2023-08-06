# Descent IV

## Flag

`pecan{b3l0w_th3_fl00r}`

## Info

Behind an accursed face lies a happier place...

### Hint 1

Another image has been hidden in this one somehow

### Hint 2

Try steghide, but you might have to work out the file type

### Hint 3

Try investigate the image within

## Solution

1. `steghide --extract -sf descent4.jpg -xf inside`
2. `file inside`
3. `mv inside inside.jpg`
4. `exiftool inside.jpg`
5. The description is in hex (706563616e7b62336c30775f7468335f666c3030727d)
6. The flag is `pecan{b3l0w_th3_fl00r}`