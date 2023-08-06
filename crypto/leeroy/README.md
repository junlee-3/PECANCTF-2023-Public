# LEEROY

The challenge description states:
`Although my last name is the key, it's anothers that conceal my secrets. yipkv{NL_UINCB_V_ZJZR_MPVUTIA}`

### Although my last name is the key

Leeroy Jenkins is a famous World of Warcraft figure, owing to the viral YouTube video. As the description hints, **JENKINS** is the key for the cipher.

### It's anothers that conceal my secrets

This part of the description is a little more cryptic and is intended to test participants' problem-solving skills.
The **Vigenere Cipher** is a renowned substitution cipher that contains a unique Caesar Cipher for each letter of the alphabet.
The cipher is named after Blaise de Vigenère, hence it is the last name that eludes to the method of encryption.

### Decryption

Now that we have the ciphertext `yipkv{NL_UINCB_V_ZJZR_MPVUTIA}`, the key `JENKINS`, and the cipher `Vigenere Cipher`, decryption can be performed.

#### To decrypt the ciphertext manually

We would first find which column has the value `Y` (first ciphertext letter) in row `J` (first key letter). In this case, the column is `P`. Since the ciphertext is lowercase, the plaintext must too be lowercase (`p`).
Next, we would find which column has the value `I` (second ciphertext letter) in row `E` (second key letter), which is `E`. Again, the ciphertext is lowercase, so the plaintext is `e`.
As you can imagine, decrypting the entire ciphertext manually is extremely laborious, so online tools are preferable.

#### To decrypt the ciphertext autonomously

Tools like [cyberchef.io](https://cyberchef.io/) or [dcode.fr](https://www.dcode.fr/vigenere-cipher) can automate this process with ease.
**Ciphertext**
yipkv{NL_UINCB_V_ZJZR_MPVUTIA}
**Plaintext**
pecan{AT_LEAST_I_HAVE_CHICKEN}
