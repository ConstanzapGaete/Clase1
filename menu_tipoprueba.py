menu=True
import os


def menup():
    print ("*************Bienvenido a EL CHILOTE*************")
    print("1- Platos")
    print("2- Bebidas")
    print("3- Imprimir boleta")
    print("4- Salir")
    try:
        opc1=int(input("Ingresa una opcion :  "))
        return opc1
    except:
        print("Error ")

def menuplatos():
    print ("*************Bienvenido a EL CHILOTE*************")
    print("1- Curanto                   $20.000")
    print("2- Mariscal                  $12.000")
    print("3- Chupe de centolla         $15.000")
    print("4- Empanadas                 $3.0000")
    try:  
        opc1=int(input("Ingresa una opcion :  "))
        return opc1
    except:
        print("Error ")

def menubebidas():
    print ("*************Bienvenido a EL CHILOTE*************")
    print("1- pisco sour            $20.000")
    print("2- Bebida lata           $12.000")
    print("3- jugo                  $15.000")
    try:
        opc1=int(input("Ingresa una opcion :  "))
        return opc1
    except:
        print("Error ")

def menuboleta():
    print("*************Bienvenido a EL CHILOTE*************")
    print("imprimir boleta ")
    print("1-Si ")
    print("2-No")
    try:  
        opc1=int(input("Ingresa una opcion :  "))
        return opc1
    except:
        print("Error ")


while menu:
    opc1=menup
    if opc1 ==1:
        menuplatos()
    if opc1==2:
        menubebidas()
    if opc1==3:
        menuboleta()
    if opc1==4:
        menu=False

os.system("cls")
print("salio del sistema")
