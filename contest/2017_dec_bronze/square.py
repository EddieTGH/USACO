with open('square.in', 'r') as fin:
 lines = fin.readlines()

rec1p1x, rec1p1y, rec1p2x, rec1p2y = map(int, lines[0].split())
rec2p1x, rec2p1y, rec2p2x, rec2p2y = map(int, lines[1].split())

maxX = rec1p1x
if maxX < rec1p2x:
    maxX = rec1p2x

if maxX < rec2p1x:
    maxX = rec2p1x

if maxX < rec2p2x:
    maxX = rec2p2x






maxY = rec1p1y
if maxY < rec1p2y:
    maxY = rec1p2y

if maxY < rec2p1y:
    maxY = rec2p1y

if maxY < rec2p2y:
    maxY = rec2p2y
        

        

minX = rec1p1x
if minX > rec1p2x:
    minX = rec1p2x

if minX > rec2p1x:
    minX = rec2p1x

if minX > rec2p2x:
    minX = rec2p2x




minY = rec1p1y
if minY > rec1p2y:
    minY = rec1p2y

if minY > rec2p1y:
    minY = rec2p1y

if minY > rec2p2y:
    minY = rec2p2y

print ("minY", minY)
print ("minX", minX)
print ("maxX", maxX)
print ("maxY", maxY)

lenX = maxX - minX
lenY = maxY - minY

if lenX > lenY:
    result = lenX ** 2
else:
    result = lenY ** 2

with open ('square.out', 'w') as fout:
    fout.write(str(result) + '\n')
