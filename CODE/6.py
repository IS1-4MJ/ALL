# SORT MY CREDENTIAL FILE

FILE = "FILE PATH"
FILE = open(FILE, 'r')
LINE = FILE.readlines()
FILE.close()

LINE2 = []
I = 0
while I < len(LINE):
    LINE2.append(LINE[I:I+4])
    I += 4



LINE2.sort(key=lambda X: X[1])
for ALL in LINE2:
    print(ALL)

OUT = ''''''
for ALL in LINE2:
    OUT += ''.join(ALL)
print(OUT)

FILE = "FILE PATH"
FILE = open(FILE, 'w')
FILE.write(OUT)
FILE.close()
