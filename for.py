#explicacion y uso de for

# for i in range(5):
#     print("hola")

# for i in range(1,6):
#      print(i)

# for i in range(5):
#      print(i+1)

# num=9
# for i in range(11):
#     print(num, "X", i ,"=",i*num)


#tablas de multiplicacion hasta el n*que uno quiera 
# j=9
# for j in range(1,11):
#     print(f"la tabla del {j}")
#     for i in range(1,11):
#         print(j, "X", i ,"=",i*j)

        # for i in range()

        ## preguntar ingresar la cantidad de notas y promediarlas


# suma=0
    
# cantnotas=int(input("ingrese la cantidad de notas "))
# for i in range(cantnotas):
#     print(f"ingrese la nota numero {i+1}")
#     nota=float(input())
#     suma=suma+nota
# prom=suma/cantnotas
# print(f"el promedio es {prom} ")
# if prom >=40:
#  print("usted aprobó")
# else: 
#  print("usted reprobó")




# cantproductos=int(input("cuantos productos llevara? "))
# total=0
# for i in range (cantproductos):
#     print('''
#           que producto llevará?
#           1.- diazepam $9000
#           2.-metametazona $18500
#           3.- oblea china $1000
#           ''')
#     op=int(input())
# if op==1:
#  print("usted lleva diazepam")
#  total=total+9000
# elif op==2:
#    print("usted lleva metametazona")
#    total=total+18500
# elif op==3:
#    print("usted lleva oblea china")
#    total=total+1000
# else:
#    print("error, seleccione una opcion valida")


# print("EL total neto es ", total)
# print("EL total mas IVA es ", total*1.19)

  
c1="hulk"
c2="ironman"
cv1=0
cv2=0

numvotos=int("ingrese un numero de votantes")


	
for i in range(numvotos):
    print(f"selecciona su candidato: 1.- {c1} , 2.- {c2}")
    voto=int(input)
if voto==1:
   # cv1=cv1+1
   cv1+=1
else:
    cv2+=1
    print(f"la cantidad de votos de {c1} es {cv1}")
    print(f"la cantidad de votos de {c2} es {cv2}")
    if cv1>cv2:
        print("el ganador es {c1}")
