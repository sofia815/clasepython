usu1=30000
clave1="messi"
usu2=40000
clave2="cristiano"
usu3=50000
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
         giro=int(input("1) 5.000 2) 10.000 3) 15.000 4)20.000"))
         if giro==1 and ca5>=1 and usu1>=5000:
             print("giro exitoso")
             usu1-=5000
             print(f"Su saldo es: {usu1}")
             ca5-=1
             print("Saldo total:",usu1)
         elif giro==2 and ca10>=1 and usu1>=10000:
             print("giro exitoso")
             usu1-=10000
             print(f"Su saldo es: {usu1}")
             ca10-=1
         elif giro==3 and ca5>=1 and ca10>=1 and usu1>=15000:
             print("giro exitoso")
             usu1-=15000
             print(f"Su saldo es: {usu1}")
             ca5-=1
             ca10-=1
         elif giro==4 and ca20>=1 and usu1>=20000:
             print("giro exitoso")
             usu1-=20000
             print(f"Su saldo es: {usu1}")
             ca20-=1
         else:
             print("billetes insuficientes")
             print(f"Su saldo es: {usu1}")
     elif op2==2:
         print(f"Su saldo es: {usu1}")
     elif op2==4:
         print("Adios")
         salir2=1

 elif op1==clave2:
     print("Bienvenido usuario 2")
     print("Ingrese opcion a realizar: ")
    
     op2=int(input("1) Sacar billetes 2) Consultar saldo 3) Salir"))
     if op2==1:
         print(f"Su saldo es: {usu2}")
         giro=int(input("1) 5.000 2) 10.000 3) 15.000 4)20.000"))
         if giro==1 and ca5>=1 and usu1>=5000:
             print("giro exitoso")
             usu2-=5000
             print(f"Su saldo es: {usu1}")
             ca5-=1
             print("Saldo total:",usu2)
         elif giro==2 and ca10>=1 and usu2>=10000:
             print("giro exitoso")
             usu1-=10000
             print(f"Su saldo es: {usu2}")
             ca10-=1
         elif giro==3 and ca5>=1 and ca10>=1 and usu2>=15000:
             print("giro exitoso")
             usu1-=15000
             print(f"Su saldo es: {usu2}")
             ca5-=1
             ca10-=1
         elif giro==4 and ca20>=1 and usu2>=20000:
             print("giro exitoso")
             usu1-=20000
             print(f"Su saldo es: {usu2}")
             ca20-=1
         else:
             print("billetes insuficientes")
             print(f"Su saldo es: {usu2}")
     elif op2==2:
         print(f"Su saldo es: {usu2}")
     elif op2==4:
         print("Adios")
         salir2=1
         
     elif op1==clave3:
      print("Bienvenido usuario 3")
     print("Ingrese opcion a realizar: ")
     op2=int(input("1) Sacar billetes 2) Consultar saldo 3) Salir"))
     if op2==1:
         print(f"Su saldo es: {usu3}")
         giro=int(input("1) 5.000 2) 10.000 3) 15.000 4)20.000"))
         if giro==1 and ca5>=1 and usu1>=5000:
             print("giro exitoso")
             usu3-=5000
             print(f"Su saldo es: {usu1}")
             ca5-=1
             print("Saldo total:",usu3)
         elif giro==2 and ca10>=1 and usu2>=10000:
             print("giro exitoso")
             usu1-=10000
             print(f"Su saldo es: {usu3}")
             ca10-=1
         elif giro==3 and ca5>=1 and ca10>=1 and usu2>=15000:
             print("giro exitoso")
             usu1-=15000
             print(f"Su saldo es: {usu3}")
             ca5-=1
             ca10-=1
         elif giro==4 and ca20>=1 and usu3>=20000:
             print("giro exitoso")
             usu1-=20000
             print(f"Su saldo es: {usu3}")
             ca20-=1
         else:
             print("billetes insuficientes")
             print(f"Su saldo es: {usu3}")
     elif op2==2:
         print(f"Su saldo es: {usu3}")
     elif op2==4:
         print("Adios")
         salir2=1
         salir2=1
 elif op1=="salir":
     salir=salir+1
 else:
     print("Ingrese una clave valida")