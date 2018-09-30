#daythe13thfallson = 13%7
#dayoftheweekmonthstartson = 31%7
#if dayoftheweekmonthstartson = 0:
#numdaysmonth_normyear = numdays
#numberdayfromstartofyear13thfallson = d13thdays


fin = open('friday.in', 'r')
N = int(fin.readline())
fin.close()
leapyear = False
nnumdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
n13thdays = [13]
index = 0
for x in range(len(nnumdays)-1):
    nnext13 = n13thdays[index]+nnumdays[x]
    n13thdays.append(nnext13)
    index += 1 
print(n13thdays)


lnumdays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
l13thdays = [13]
index = 0
for x in range(len(lnumdays)-1):
    lnext13 = l13thdays[index]+lnumdays[x]
    l13thdays.append(lnext13)
    index += 1
print(l13thdays)
satcount = suncount = moncount = tuecount = wedcount = thucount = fricount  = 0
counter = [0, 0, 0, 0, 0, 0, 0]
def finddays(n13thdays, counter):
    index = 0
    for x in n13thdays:
        if n13thdays[index] % 7 == 0:
            #suncount += 1
            counter[0] += 1
        if n13thdays[index] % 7 == 1:
            #moncount += 1
            counter[1] += 1
        if n13thdays[index] % 7 == 2:
            #tuecount += 1
            counter[2] += 1
        if n13thdays[index] % 7 == 3:
            #wedcount += 1
            counter[3] += 1
        if n13thdays[index] % 7 == 4:
            #thucount += 1
            counter[4] += 1
        if n13thdays[index] % 7 == 5:
            #fricount += 1 
            counter[5] += 1
        if n13thdays[index] % 7 == 6:
            #satcount += 1
            counter[6] += 1
        index += 1
    return counter
'''
print("friday: ", fricount)
print("saturday: ", satcount)
print("sunday: ", suncount)
print("tuesday: ", tuecount)
print("monday: ", moncount)
print("wednesday: ", wedcount)
print("thursday: ", thucount)
'''
inityear = 1900
for i in range(0, N):
    curryear = inityear + i 
    if curryear % 100 == 0: 
        if curryear % 400 == 0:
            leapyear = True
    elif curryear % 4 == 0:
        leapyear = True
        print("current year: ", curryear)
    if leapyear == True:
        counter = finddays(l13thdays, counter)
        leapyear = False
    else:
        counter = finddays(n13thdays, counter)
    for k in range(len(n13thdays)):
        n13thdays[k] += 1
        l13thdays[k] += 1
print("n13thdays: ", n13thdays)
'''
print("friday: ", fricount)
print("saturday: ", satcount)
print("sunday: ", suncount)
print("tuesday: ", tuecount)
print("monday: ", moncount)
print("wednesday: ", wedcount)
print("thursday: ", thucount)'''
print(counter)
