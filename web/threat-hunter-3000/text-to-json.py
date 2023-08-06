import re
import json

file1 = open("./public/apache.logs")
file2 = open("./public/apache.json", 'w+')
data = file1.read().split('\n')

regex = '^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+)\s*(\S+)?\s*" (\d{3}) (\S+)'
fields = ['ip','ui','usr','@timestamp','method','rline','ver','status','size']
x = int(len(data) * 0.3)
actions = []

def function(inp):
    m = re.match(regex, inp)
    if m:
        data1 = m.groups(0)
        data2 = dict(zip(fields, data1))
        actions.append(data2)

for i in range(0,50):
    function(data[i])

j = json.dumps(actions)
file2.write(j)
