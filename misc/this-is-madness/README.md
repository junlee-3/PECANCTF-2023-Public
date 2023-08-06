# This is madness

The file 300.txt contains 156300 characters.
The flag description quotes a line from the movie 300, providing a clue to how to solve the challenge.

A passage can be extracted by reading every 300th character of the 300.txt file.
This can be done any number of ways, but perhaps the most simple utilises string slicing in Python:

```Python
text = open('300.txt', 'r').read()
# print first char at index 299 (300th char)
# then every 300th char after that
print(text[299::300])
# Choose your next words carefully, Leonidas. They may be your last as king. 'Earth and water'? Madman! You're a madman! Earth and water? You'll find plenty of both down there. No man, Persian or Greek, no man threatens a messenger! You bring the crowns and heads of conquered kings to my city steps. You insult my queen. You threaten my people with slavery and death! Oh, I've chosen my words carefully, Persian. Perhaps you should have done the same! This is blasphemy! This is madness! pecan{Madness...?_This_is_Sparta!}
```

Alternatively, a less efficient iteration method can be employed:

```Python
text = open('300.txt', 'r').read()
count = 0
for char in text:
    count += 1
    if count % 300 == 0:
        print(char, end='')
# Choose your next words carefully, Leonidas. They may be your last as king. 'Earth and water'? Madman! You're a madman! Earth and water? You'll find plenty of both down there. No man, Persian or Greek, no man threatens a messenger! You bring the crowns and heads of conquered kings to my city steps. You insult my queen. You threaten my people with slavery and death! Oh, I've chosen my words carefully, Persian. Perhaps you should have done the same! This is blasphemy! This is madness! pecan{Madness...?_This_is_Sparta!}
```

The end of the output reveals the hidden flag, `pecan{Madness...?_This_is_Sparta!}`
