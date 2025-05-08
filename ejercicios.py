### VOTATOON###
# # Designe 2 cantdidatos. Pregunte cuanto votantes son
# # por cada votante , debe peguntar por quin votrá
# # cuente la cantidad de votos y muestre los resultados
# # definir quien ganó la votacion. Considere empate
# import time


# c1="Fiona"
# c2="shrek"
# cand1=0
# cand2=0


# totalvotantes=int(input("cuantos votantes son? "))

# for i in range (totalvotantes):
#         print(f"seleccione su candidato 1.- {c1}, 2.- {c2}" )
#         voto=int(input("por quien votará? "))

#         if  voto==1:
#             print("votó por fiona")
#             cand1+=1
            
            
#         elif voto==2:
#                 print("votó por shrek")
#                 cand2+=1
#                #10 time.sleep(2)
#         else:
#             print("voto invalido")        
# print(f"la cantidad de votos de {c1} es {cand1} ")
# print(f"la cantidad de votos de {c2} es {cand2} ")
# if cand1>cand2:
#             print("el ganador es ", c1 )
# elif cand2>cand1:
#         print("el ganador es ", c2)
# # elif cand1==cand2:
# else:
#             print(" es un empate ")
        

# ### Pedir dia y mes de nacimiento y mostrar el signo zodiacal###
import random
import time
# dianac=int(input("ingrese su dia de nacimiento "))
# mesnac=int(input("ingrese su mes de nacimiento "))

# if (dianac>=21 and mesnac==3) or (mesnac==4 and dia<=19):
#   print("usted es aries")
# elif (dianac>=20 and mesnac==4) or (mesnac==5 and dianac<=20):
#   print("usted es tauro")
# elif (dianac>=21 and mesnac==5) or mesnac==6 and dianac<=20:
#   print("usted es geminis")
# elif (dianac>=21 and mesnac==6) or (mesnac==7 and dianac<=22):
#   print("usted es cancer")
# elif (dianac>=23 and mesnac==7) or (mesnac==8 and dianac<=22):
#   print("ustes es leo")
# elif (dianac>=23 and mesnac==8) or (mesnac==9 and dianac<=22):
#   print("usted es virgo")
# elif (dianac>=23 and mesnac==9) or (mesnac==10 and dianac<=22):
#   print("usted es libra") 
# elif (dianac>=23 and mesnac==10) or (mesnac==11 and dianac<=21): 
#   print("usted es escorpio")
# elif (dianac>=22 and mesnac==11) or (mesnac==12 and dianac<=21):
#   print("usted es sagitario")
# elif (dianac>=22 and mesnac ==12) or (mesnac==1 and dianac<=19):
#   print("usted es capricornio")
# elif (dianac>=20 and mesnac==1) or (mesnac==2 and dianac<=18):
#   print("usted es acuario")
# elif (dianac>=19 and mesnac==2) or (mesnac==3 and dianac<=20):
#   print("usted es piscis")
# else: 
#   print("fecha invalida")      


##### pida al usuario 2 digitos verificando que el segundo sea mayor#####
# Genere un numero aleatoreo entre esos digitos
# ► e imprima esa candidad de veces el simbolo  ▄ (alt+220)



#### Calcular el puntaje de credito####
# De bede calcular que tanto credito tiene una persona
# en cierta entidad financiera, debera considerar
# cantidad de ingresos, nivel educacional y nacionalidad
# Cantidad de ingresos
# 500.000 a 1.000.000 : 300.000
# 1.000.000 a 1.500.000: 650.000
# 1.500.001 o mas : 1.000.000
# Nivel Educacional 
# Basico : x1, medio: x1.3 , superior: x1.5
# Nacionalidad 
# Chilena : +300.000, Extranjero: +0



#suma=0 no es necesario declararla aparte ya que se declara en canting



# Crear un cajero automatico#####
# Tener en cuenta cajas de billetes de 5000 , 10000 y 20000
# Cada caja tine 30 billetes. Verificar si el monto solicitado
# Esta disponible en el cajero.Verificar si el monto solicidado
# es posible por el multiplo de los billetes disponibles
# Al terminar cada transaccion, debe mostrar saldo Disponible
# Debe haber 3 usuarios cada uno son su saldo correspondiente
# Usar clave secreta para iniciar y segun la clave 
# asociar el saldo disponible

# totalasacar=350000
# clave=1234
# intentos=3
# while totalasacar==0:
#   print("bienvenido al cajero")
#   for i in range(3): 
      
#    Clave=int(input("ingrese su clave, tiene 3 intentos"))
# if Clave==clave:
#          print("puede ingresar")
#          intentos-=intentos
# elif 
# print("clave incorrecta, vuelva a intentarlo"):
# else: 
#          print("cuenta bloqueada")
     
#          for i in range(3):
#                montosol=int(input("cuanto dinero quiere sacar?"))
#              #hay 10 billetes de 5mil, 10 de 10mil y 10 de 20mil
#          if montosol>=5000 and montosol<=350000:
#              print("saldo disponible")
#              totalasacar-=montosol
#              print("le quedan $",totalasacar, "para retirar")
#          else:
#            print("no hay saldo dispoible")



usu1=6000
clave1="messi"
usu2=40000
clave2="cristiano"
usu3=12000
clave3="alexis"
ca10=30
ca20=30
ca5=30
salir=0
salir2=0
cajero=ca10+ca20+ca5


while salir==0:
 op1=input("Bienvenido ingrese su palabra secreta: ").strip().lower()
 if op1==clave1:
  while salir2==0:
     print("Bienvenido usuario 1")
     print("Ingrese opcion a realizar: ")
     op2=int(input("1) Sacar billetes 2) Consultar saldo 3) Salir"))
     if op2==1:
         print(f"Su saldo es: {usu1}")
         giro=int(input("Ingrese un numero a retirar  "))
         if giro==1 and ca5>=1 and usu1>=5000:
             print("giro exitoso")
             usu1-=5000
             ca5-=1
        
            print("le quedan" usu1)
        elif giro==2:
         
         usu1>=giro and giro<=cajero:
             print("")
     elif op2==2:
         print(f"Su saldo es: {usu1}")
     elif op2==3:
         print("Adios")
         salir2=1
     
 elif op1==clave2:
     print("Bienvenido usuario 2")
     print("Ingrese opcion a realizar: ")
     op2=int(input("1) Sacar billetes 2) Consultar saldo 3) Salir"))
     if op2==1:
         print(f"Su saldo es: {usu2}")
         giro=int(input("Ingrese un numero a retirar"))
         if usu2>=giro and giro<=cajero:
            
             print("")
     elif op2==2:
         print(f"Su saldo es: {usu2}")
     elif op2==3:
         print("Adios")
         salir2=1
 elif op1==clave3:
     print("Bienvenido usuario 3")
     print("Ingrese opcion a realizar: ")
     op2=int(input("1) Sacar billetes 2) Consultar saldo 3) Salir"))
     if op2==1:
         print(f"Su saldo es: {usu3}")
         giro=int(input("Ingrese un numero a retirar"))
         if usu3>=giro and giro<=cajero:
             print("")
     elif op2==2:
         print(f"Su saldo es: {usu3}")
     elif op2==3:
         print("Adios")
         salir2=1
 elif op1=="salir":
     salir=salir+1
 else:
     print("Ingrese una clave valida")