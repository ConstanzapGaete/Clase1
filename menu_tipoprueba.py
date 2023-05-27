menu=True
import os
opcion_general=0
opcion_platos=0
opcion_bebidas=0
opcion_boleta=0


def menup():
    print ("*************Bienvenido a EL CHILOTE*************")
    print("1- Platos")
    print("2- Bebidas")
    print("3- Imprimir boleta")
    print("4- Salir")
    try:
        opcion_general=int(input("Ingresa una opcion :  "))
        return opcion_general
    except:
        print("Error ")

def menuplatos():
    print ("*************Bienvenido a EL CHILOTE*************")
    print("1- Curanto                   $20.000")
    print("2- Mariscal                  $12.000")
    print("3- Chupe de centolla         $15.000")
    print("4- Empanadas                 $3.0000")
    try:  
        opcion_platos=int(input("Ingresa una opcion :  "))
        return opcion_platos
    except:
        print("Error ")

def menubebidas():
    print ("*************Bienvenido a EL CHILOTE*************")
    print("1- pisco sour            $20.000")
    print("2- Bebida lata           $12.000")
    print("3- jugo                  $15.000")
    try:
        opcion_bebidas=int(input("Ingresa una opcion :  "))
        return opcion_bebidas
    except:
        print("Error ")

def menuboleta():
    print ("*************Bienvenido a EL CHILOTE*************")
    print("imprimir boleta ")
    print("1-Si ")
    print("2-No")
    try:  
        opcion_boleta=int(input("Ingresa una opcion :  "))
        return opcion_boleta
    except:
        print("Error ")

menu1=menup()
menu2=menuplatos()
menu3=menubebidas()
menu3=menuboleta()
while menu:
    if menu1<0 and menu1>2:
        menup()
    if menu2 <1 and menu2>3:
        menuplatos()
    if menu3 <2 and menu3 >4:
        menubebidas()
print("salio del sistema")