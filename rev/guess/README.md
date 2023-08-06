# Guess Writeup

1. Open the executable in a debugger
2. Inspect the area where the flag is supposed to be printed
3. Notice that a whole bunch of array writes are performed which seem to have ASCII values. (Most debuggers will show the code point)
4. Add the sequence together
5. Profit!
