#hint > Do not waste your time here !

import hashlib

sh = "a86496f3ee91ba2dfddd66c7a40faf924ef5258373ecf53b5e760c6c09bc42582a87db2139a8528a960a6c1d7781c410a694d6f116011e763b049c1c4ca7d6f6"
slt="?so#&"
#print(Location coords)
ppr = [6732,12312,11349,10197,6161,1984,9744,9797,11979,10670,11110,8118,5586,12753,4455,5151,2048,10092,4365,9317,10670,11110,8250]

print("Hello Hero! \n Crack me if you can ;) \n I may look young and 6'4, but I'm actually 40 ish. \n---------------------------------------------------------\n3b1485d981724ce400375c951873e6888e549c5baa65103b0b429361976774c0\n---------------------------------------------------------")
while(1):
    val = input("Who am I? ")

    h = hashlib.sha3_512()
    h.update(bytes(val+slt, 'utf-8'))

    if(h.hexdigest()==sh):
        print("Nice !!! here's your reward :) \n___________________________")
        val*=5
        for i,v in enumerate(ppr):
            print(chr(int(v/ord(val[i]))),end="")
        print("\n___________________________")
        break
    else:
        print("Wrong! Try again.")
