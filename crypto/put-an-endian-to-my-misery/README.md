# Put an endian to my misery

The flag has had its endianness swapped (with a word length of 4)
Using a tool like [cyberchef.io](https://cyberchef.io/), the endianness can be swapped revealing the flag.
Alternatively, conversion can be done manually, e.g.

**Ciphertext flag**
`acep_1{n4wl4g_5yt_t3t_3hm_0wd3x1!pu_}`

**Separating the flag into word lengths of 4**
`acep _1{n 4wl4 g_5y t_t3 t_3h m_0w d3x1 !pu_}`

**Swapping endianness for each word**
`peca n{1_ 4lw4 y5_g 3t_t h3_t w0_m 1x3d _up!}`

**Removing spaces to reveal the flag**
`pecan{1_4lw4y5_g3t_th3_tw0_m1x3d_up!}`
