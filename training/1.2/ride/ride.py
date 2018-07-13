"""
ID: EddieTGH 
LANG: PYTHON3
TASK: ride 
"""
fin = open ('ride.in', 'r')
line1 = fin.readline().strip()
print ("line1=", line1)
line2 = fin.readline().strip()
print ("line2=", line2)

value1 = 1
for letter in line1:
    print("letter:", letter, "convert to ascii code: ", ord(letter))
    print ("convert to our number: ", ord(letter) - ord('A') + 1)
    value1 *= ord(letter) - ord('A') + 1
print("value1=" , value1)


value2 = 1
for letter in line2:
    value2 *= ord(letter) - ord ('A') + 1
print ("value2=", value2)

value1 %= 47
value2 %= 47
print("after mod, value 1=", value1)
print("afer mod, value2=", value2)

if value1 == value2:
    result = "GO"
else:
    result = "STAY"


fout = open ('ride.out', 'w')
fout.write (result + '\n')
fout.close()

