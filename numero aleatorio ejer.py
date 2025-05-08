import random

n1=0
n2=0

while n1>=n2:
 n1=int(input("ingrese un numero"))
 n2=int(input("ingrese un numero mayor al anterior"))
 if n2>n1:
  numero=random.randint(n1,n2)
  print(" ▄  "*numero)


  
  
  

