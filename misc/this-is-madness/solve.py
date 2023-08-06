# Reveals the flag by reading the 300.txt and printing every 300th character

# String slicing method
text = open('300.txt', 'r').read()
# print first char at index 299 (300th char)
# then every 300th char after that
print(text[299::300])

# Iteration method
text = open('300.txt', 'r').read()
count = 0
for char in text:
    count += 1
    if count % 300 == 0:
        print(char, end='')