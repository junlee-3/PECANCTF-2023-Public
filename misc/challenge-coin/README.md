The back of the coin has the challenge

* The inner symbols are a [Templar cipher](https://www.dcode.fr/templars-cipher): TRYEVERYOTHER
* Take every other (second) character on the outer ring. You'll get two strings: WH3R3ISTH3T0UC4N and MD5ANDXORMAYHELP
* In [Cyberchef](https://gchq.github.io/CyberChef/), hash WH3R3ISTH3T0UC4N with the MD5 operation: cb85462fccb075994bc51e42278cd7e7
* Then convert the letters and numbers with the From Hex operation
* Use the XOR operation with the MD5 hash as the key, in Hex mode: "Bring this flag to 2024: PECAN4WASGR8"
* The flag is pecan{PECAN4WASGR8}
