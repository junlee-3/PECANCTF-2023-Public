# Climbing

In this challenge, participants will decrypt a stream cipher.
The stream cipher in this challenge uses a very basic key which simply adds the ASCII order of a
given character with its position in the provided message, returning a series of numbers as
the ciphertext.

The ciphertext was calculated using the following formula:
`ciphertext[i] = ord(message[i]) + i`

The plaintext can be calculated by reversing the cipher operation:
`plaintext[i] = chr(ciphertext[i] - i)`

Participants may correctly interpret the hint 'Climbing' in relation to the cipher's
key which increments with each consecutive character (starting at zero).

Participants may choose to
write a basic Python script, such as `solution_do_not_distribute.py` (**which is not to be shown to participants**), to enumerate over each character, decrypt it, and print the flag as plaintext.
They may also manually observe patterns in the ciphertext by referencing an ASCII table.
