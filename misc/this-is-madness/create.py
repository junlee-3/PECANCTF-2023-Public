# Creates the 300.txt file

import random

flag = "Choose your next words carefully, Leonidas. They may be your last as king. 'Earth and water'? Madman! You're a madman! Earth and water? You'll find plenty of both down there. No man, Persian or Greek, no man threatens a messenger! You bring the crowns and heads of conquered kings to my city steps. You insult my queen. You threaten my people with slavery and death! Oh, I've chosen my words carefully, Persian. Perhaps you should have done the same! This is blasphemy! This is madness! pecan{Madness...?_This_is_Sparta!}"
string = ""

for char in range(len(flag)):
    for i in range(299):
        rand_char = chr(random.randint(33, 126))
        string = string + rand_char
    string = string + flag[char]

f = open('300.txt', 'w')
f.write(string)
f.close()