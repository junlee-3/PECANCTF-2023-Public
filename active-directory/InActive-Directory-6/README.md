Flag:
> pecan{Administrator_iloveanime!!!}

Solution:

1. One of the files provided is a kerberoast output.
2. Put the file into John or Hashcat.
3. Run "hashcat -m 13100 kerberoast.txt rockyou.txt -O" with rockyou.
4. Password is crackable.

> hashcat -m 13100 kerberoast.txt rockyou.txt -O

![](images/Crack-Hash.png)
