# Descent IV

## Flag

`pecan{4_rubb3r_r00m_w1th_f4ncy_c4t5}`

## Info

Crazy? I was crazy once

### Hint 1

Have you tried EXIF?

### Hint 2

Have you pasted that description into notepad?

### Hint 3

How long is it?

### Hint 4

How can we hide text in text?

### Hint 5

https://330k.github.io/misc_tools/unicode_steganography.html

It's also a binary encoding based on zero-width spaces so they can
decode it themselves but if they start running out of time this
will be helpful.

## Solution

1. `exiftool descent5.jpg`
2. EXIF Description: 'Crazy‌‌‌‌‍‬‌‬?‌‌‌‌‌﻿‍‬ I‌‌‌‌‍‬‍‍‌‌‌‌‌﻿‍‌ ‌‌‌‌‌﻿‬‌‌‌‌‌‌﻿‍‍was‌‌‌‌‌﻿‌﻿ ‌‌‌‌‌﻿‍‬crazy ‌‌‌‌‌﻿‍‬once.‌‌‌‌‌﻿‍﻿ ‌‌‌‌‍‬‌‍‌‌‌‌‌﻿‍‌‌‌‌‌‌﻿‌‬‌‌‌‌‌﻿‌﻿They‌‌‌‌‌﻿‍‍ ‌‌‌‌‌﻿‍‬‌‌‌‌‌﻿‌‌locked me‌‌‌‌‌﻿‌﻿‌‌‌‌‌﻿‬‌‌‌‌‌‌﻿‌﻿ ‌‌‌‌‍‬‌﻿in a ‌‌‌‌‌﻿‍‬room‌‌‌‌‍‬‌‍.‌‌‌‌‌﻿‍‍‌‌‌‌‌﻿‌‌‌‌‌‌‌﻿‍﻿ ‌‌‌‌‌﻿‌‬‌‌‌‌‌﻿‍‌‌‌‌‌‌﻿‬‌A ‌‌‌‌‌﻿‍‌rubber‌‌‌‌‌﻿‌﻿‌‌‌‌‌﻿‍‬ room. ‌‌‌‌‍‬‌‍‌‌‌‌‌﻿‍﻿A rubber room‌‌‌‌‌﻿‬‍‌‌‌‌‌﻿‍‍‌‌‌‌‌﻿‌‬ with‌‌‌‌‌﻿‌﻿ rats. A ‌‌‌‌‌﻿‬‌rubber room‌‌‌‌‌﻿‍‍‌‌‌‌‍‬‍‌ ‌‌‌‌‌﻿‍‬‌‌‌‌‌﻿‌‬‌‌‌‌‌﻿‍‌with‌‌‌‌‌﻿‍‌‌‌‌‌‌﻿‍‌ ‌‌‌‌‍‬‍‌rubber ‌‌‌‌‌﻿‍‌rats. ‌‌‌‌‌﻿‬‌Rubber‌‌‌‌‌﻿‍‬‌‌‌‌‌﻿‬‍ rats‌‌‌‌‌﻿‌﻿‌‌‌‌‌﻿‌‍ ‌‌‌‌‌﻿‌﻿and‌‌‌‌‌﻿‌‍‌‌‌‌‌﻿‍‬‌‌‌‌‌﻿‬‌ ‌‌‌‌‌﻿‍﻿rubber‌‌‌‌‌﻿‍﻿‌‌‌‌‌﻿‍‬ ‌‌‌‌‍‬‍‌mats.‌‌‌‌‌﻿‍‬ ‌‌‌‌‌﻿‍‌The ‌‌‌‌‌﻿‍‬cats‌‌‌‌‌﻿‍‬ make‌‌‌‌‌﻿‍‬ ‌‌‌‌‌﻿‌‬me‌‌‌‌‌﻿‍‍ crazy. ‌‌‌‌‌﻿‬‌‌‌‌‌‌﻿‍‌‌‌‌‌‍‬‍‍‌‌‌‌‌﻿‍‌Crazy ‌‌‌‌‌﻿‬‍‌‌‌‌‌﻿‍‬‌‌‌‌‌﻿‍‬‌‌‌‌‌﻿‍‌‌‌‌‌‌﻿‬‌cats.‌‌‌‌‌﻿‍‍ Crazy‌‌‌‌‌﻿‌‬‌‌‌‌‌﻿‍‬‌‌‌‌‌﻿‍‬ ‌‌‌‌‌﻿‍‬cats‌‌‌‌‌﻿‍‬‌‌‌‌‌﻿‍‌‌‌‌‌‌﻿‬‌ and‌‌‌‌‌﻿‍‌‌‌‌‌‍‬‍‍ crazy mats.‌‌‌‌‌﻿‍‌‌‌‌‌‍‬‍‬‌‌‌‌‌﻿‍‬‌‌‌‌‌﻿‍‬‌‌‌‌‌﻿‍‍‌‌‌‌‌﻿‍‌‌‌‌‌‌﻿‍‍‌‌‌‌‌﻿‍‬‌‌‌‌‌﻿‍‬'
3. When pasted in notepad or Python, some analysis makes it apparant the string is far longer than it should be.
4. The mentioned tool will reveal the following string: b6e4853667a423560383c6a507248436a7952385d62444d4869313168776d646662584e496648526666484e4f6654566
5. This must be:
   1. Reversed
   2. Converted from hex
   3. Converted from base64
   4. Reversed
   5. Caesar-shifted by -14