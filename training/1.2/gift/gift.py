"""
ID: EddieTGH 
LANG: PYTHON3
TASK: gift1 
"""


with open('gift1.in', 'r') as fin:
 lines = fin.readlines()

inputIndex = 0
N = int(lines[inputIndex])
inputIndex += 1

print(N)
print("inputIndex=", inputIndex)
names = []
dict = {}
for index in range(N):
    print("inputIndex=", inputIndex, " index=", index, " inputIndex=", inputIndex)
    name = lines[inputIndex].strip()
    inputIndex += 1
    print("name=", name)
    names.append(name)
    dict[name] = 0
    print("names=", names)
    print("dict=", dict)

for indexGiver in range(N):
    print("indexGiver=", indexGiver)
    nameGiver = lines[inputIndex].strip()
    print("nameGiver=", nameGiver)
    inputIndex += 1
    money, count = map(int, lines[inputIndex].split())
    if count == 0: 
        moneydist = 0
    else: 
        moneydist = money // count
    inputIndex += 1 
    for indexReceiver in range(count):
        print("indexReceiver=", indexReceiver)
        nameReceiver = lines[inputIndex].strip()
        inputIndex += 1
        dict[nameReceiver] += moneydist
    dict[nameGiver] -= moneydist * count

print("final dict=", dict)

with open ('gift1.out', 'w') as fout:
    for person in names:
        fout.write(person + ' ' + str(dict[person]) + '\n')
