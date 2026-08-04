#letter A
print("Letter A")
rows=6
columns=7
for i in range(rows):
 for j in range(columns):
  if ((i==0 and j==3) or
     (i==1 and (j==2 or j==4))or
     (i==2 and (j==1 or j==5))or
     (i==3 and j>=0 and j<=6) or
     (i>=4 and (j==0 or j==6))):
     print("*",end="")
  else:
    print(" ",end="")
 print() 

#Letter B
print("Letter B")
rows=7
columns=5
for i in range(rows):
  for j in range(columns):
    if((j==0)or
      (i==0 and j<=3)or
      (i==3 and j<=3)or
      (i==6 and j<=3)or
      ((i==1 or i==2 or i==4 or i==5) and j==4)):
      print("*",end="")
    else:
      print(" ",end="")
  print()

#Letter c
print("Letter C")
rows=7
columns=6
for i in range(rows):
  for j in range(columns):
    if((i==0 and j>0)or
        (i>0 and i<6 and j==0)or
        (i==6 and j>0)):
        print("*",end="")
    else:
        print(" ",end="")
  print()
#Letter D
print("Letter D")
rows=7
columns=6
for i in range(rows):
  for j in range(columns):
    if((j==0)or
       (i==0 or i==6)and(j<=3)or
       (i==1 or i==5)and(j==4)or
       (i==2 or i==3 or i==4)and(j==5)):
     print("*",end="")
    else:
      print(" ",end="")
  print("")
#Letter E
print("Letter E")
rows=7
columns=5
for i in range(rows):
  for j in range(columns):
    if ((j==0)or
        (i==0)or
        (i==3)or
        (i==6)):
      print("*",end="")
    else:
      print(" ",end="")
  print("")

#Letter F
print("Letter F")
rows=7
columns=5
for i in range(rows):
  for j in range(columns):
    if ((j==0)or
        (i==0)or
        (i==3)):
      print("*",end="")
    else:
      print(" ",end="")
  print("")


#Letter G
print("Letter G")
rows=7
columns=6
for i in range(rows):
  for j in range(columns):
    if ((i==0 and j>0)or
        (i>0 and i<6 and j==0)or
        (i==3 and j>2)or
        ((i==4 or i==5) and j==5)or
        (i==6 and j>0)):
      print("*",end="")
    else:
      print(" ",end="")
  print()
#Letter H
print("Letter H")
rows=7
columns=5
for i in range(rows):
  for j in range(columns):
    if((j==0 and i>=0)or
       (j==4 and i>=0)or
       (i==3 and j>=0)):
      print("*",end="")
    else:
      print(" ",end="")
  print("")
#Letter I
print("Letter I")
rows=7
columns=6
for i in range(rows):
  for j in range(columns):
    if ((i==0 and j>=0)or
        (j==2 and i>=0)or
        (i==6 and j>=0)):
      print("*",end="")
    else:
      print(" ",end="")
  print("")
#Letter j
print("Letter J")
rows=7
columns=5
for i in range(rows):
  for j in range (columns):
    if((i==0 and j>=0)or
       (j==4 and i>=0)or
       (j==0 and(i==4 or i==5))or
       (i==6 and j>0 and j<=3)):
      print("*",end="")
    else:
      print(" ",end="")
  print("")
#Letter K
print("Letter K")
rows=7
columns=6
for i in range(rows):#0
  for j in range (columns):#0
    if((j==0 and i>=0)or
       (j==5 and i==0)or
       (j==4 and i==1)or
       (j==3 and i==2)or
       (j==2 and i==3)or
       (j==3 and i==4)or
       (j==4 and i==5)or
       (j==5 and i==6)):
      print("*",end="")
    else:
      print(" ",end="")
  print("")

#Letter L
print("Letter L")
rows=7
columns=6
for i in range(rows):
  for j in range (columns):
    if((j==0 and i>=0)or
       (j>=0 and i==6)):
      print("*",end="")
    else:
      print(" ",end="")
  print("")
#Letter M
print("Letter M")
rows=7
columns=7
for i in range(rows):
  for j in range (columns):
    if((i>=0 and j==0)or
      (i>=0 and j==6)or
      (i==1 and (j==1 or j==5))or
      (i==2 and(j==2 or j==4))or
      (i==3 and j==3)):
       print("*",end="")
    else:
      print(" ",end="")
  print("")


#Letter N
print("Letter N")
rows=7
columns=7
for i in range(rows):
  for j in range (columns):
    if((i>=0 and j==0)or
          (i>=0 and j==6)or
          (i==1 and j==1)or
          (i==2 and j==2)or
          (i==3 and j==3)or
          (i==4 and j==4)or
          (i==5 and j==5)):
        print("*",end="")
    else:
         print(" ",end="")
  print("")
#letter O
print("Letter O")
rows=7
columns=7
for i in range(rows):
  for j in range(columns):
    if((i==0 and j>0 and j<6)or
       (i==6 and j>0 and j<6)or
       (j==0 and i>0 and i<6)or
       (j==6 and i>0 and i<6)):
      print("*",end="")
    else:
      print(" ",end="")
  print("")
#Letter P
print("Letter P")
rows=7
columns=5
for i in range(rows):
  for j in range(columns):
    if((i==0 and j>=0)or
       (i>=0 and j==0)or
       (i==3 and j>=0)or
       ((i==1 or i==2) and j==4)):
      print("*",end="")
    else:
      print(" ",end="")
  print("")
#Letter Q
print("Letter R")
rows=8
columns=8
for i in range(rows):
  for j in range(columns):
    if((i==0 and j>0 and j<6)or
       (i==6 and j>0 and j<6)or
       (j==0 and i>0 and i<6)or
       (j==6 and i>0 and i<6)or
       (j==7 and i==6)or
       (j==4 and i==4)or
       (j==5 and i==5)):
      print("*",end="")
    else:
      print(" ",end="")
  print("")

#Letter R
print("Letter R")
rows=7
columns=5
for i in range(rows):
  for j in range(columns):
    if((i==0 and j>=0)or
       (i==3 and j>=0)or
       (j==4 and (i==1 or i==2))or
       (j==0 and i>=0)or
       (j==2 and i==4)or
       (j==3 and i==5)or
       (j==4 and i==6)):
      print("*",end="")
    else:
      print(" ",end="")
  print("")
#letter S
print("Letter S")
rows=7
columns=5
for i in range(rows):
  for j in range(columns):
    if((i==0 and j>=0)or
       (i==3 and j>=0)or
       (j==0 and (i>=0 and i<=3))or
       (i==6 and j>=0)or
       (j==4 and i>=3)):
      print("*",end="")
    else:
      print(" ",end="")
  print("")

#Letter T
print("Letter V")
rows=7
columns=5
for i in range(rows):
  for j in range(columns):
    if ((i==0 and j>=0)or
        (i>=0 and j==2)):
      print("*",end="")
    else:
      print(" ",end="")
  print("")
#Letter U
print("Letter U")
rows=7
columns=5
for i in range(rows):
  for j in range (columns):
    if((i>=0 and j==0)or
      (i>=0 and j==4)or
      (i==6 and j>=0)):
      print("*",end="")
    else:
      print(" ",end="")
  print("")
#Letter V
print("Letter V")
rows=7
columns=11
for i in range(rows):
  for j in range(columns):
    if(i==0 and (j==0 or j==10)or
      (i==1 and (j==1 or j==9))or
      (i==2 and (j==2 or j==8))or
      (i==3 and (j==3 or j==7))or
      (i==4 and (j==4 or j==6))or
      (i==5 and (j==5 or j==5))):
      print("*",end="")
    else:
      print(" ",end="")
  print("")

#Letter W
print("Letter W")
rows=7
columns=7
for i in range(rows):
  for j in range (columns):
    if ((i>=0 and j==0)or
        (i>=0 and j==6)or
        (i==3 and j==3)or
        (i==4 and (j==2 or j==4))or
        (i==5 and (j==1 or j==5))):
      print("*",end="")
    else:
      print(" ",end="")
  print("")

#Letter X
print("Letter X")
rows=7
columns=7
for i in range(rows):
  for j in range(columns):
    if ((i==0 and (j==0 or j==6))or
        (i==1 and (j==1 or j==5))or
        (i==2 and (j==2 or j==4))or
        (i==3 and j==3)or
        (i==4 and (j==2 or j==4))or
        (i==5 and (j==1 or j==5))or
        (i==6 and (j==0 or j==6))):
      print("*",end="")
    else:
      print(" ",end="")
  print("")
#Letter Y
print("letter Y")
rows=7
columns=7
for i in range(rows):
  for j in range(columns):
    if ((i==0 and (j==0 or j==6))or
        (i==1 and (j==1 or j==5))or
        (i==2 and (j==2 or j==4))or
        (i==3 and j==3)or
        (i>=4 and j==3)):
      print("*",end="")
    else:
      print(" ",end="")
  print("")
#Letter Z
print("Letter Z")
rows=7
columns=7
for i in range(rows):
  for j in range(columns):
    if ((i==0 and j>=0)or
        (i==6 and j>=0)or
        (i==1 and j==5)or
        (i==2 and j==4)or
        (i==3 and j==3)or
        (i==4 and j==2)or
        (i==5 and j==1)):
      print("*",end="")
    else:
      print(" ",end="")
  print("")
