def SinTD(Palabra):
    import unicodedata
    Alfabetom =("abcdefghijklmnñopqrstuvwxyz")
    AlfabetoM=("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
    sinTD=[]
    for letra in Palabra:
        if letra=="Ñ" or letra=="ñ":
            sinTD.append(letra)
        else:
            sin=unicodedata.normalize("NFD",letra)
            for i in sin:
                if unicodedata.category(i) != 'Mn':
                    sinTD.append(i)
    respuesta="".join(sinTD)
    return respuesta

def depurar(Palabra):
    Alfabetom =("abcdefghijklmnñopqrstuvwxyz")
    AlfabetoM=("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
    Corregido=[]
    for letra in Palabra:
        if letra in Alfabetom or letra in AlfabetoM:
            Corregido.append(letra)
        elif letra==" ":
            Corregido.append(letra)
    Respuesta="".join(Corregido)
    return Respuesta

def Minus(F):
    m=F.lower()
    return m

def CodiVigenere(mfra3, mcla3):

    Alfabeto =("abcdefghijklmnñopqrstuvwxyz")
    EspacioF=[]
    EF=mfra3.find(" ")
    EspacioC=[]
    EC=mcla3.find(" ")

    Num1=[]
    for letra in mfra3:
        if letra in Alfabeto:
            X=Alfabeto.find(letra)
            Num1.append(X)
    while EF!=-1:
        EspacioF.append(EF)
        EF=mfra3.find(" ",EF+1)

    Num2=[]
    while len(Num1)>len(Num2): 
        for letra in mcla3:
            if letra in Alfabeto:
                X=Alfabeto.find(letra)
                Num2.append(X)
            else:
                if letra==" ":  
                    EspacioC.append(mcla3.index(letra))
    while EC!=-1:
        EspacioC.append(EC)
        EC=mcla3.find(" ",EC+1)


    Num3=[]
    for a, b in zip(Num1, Num2):
        Num3.append((a+b)%27)


    Encriptado=[]
    for num in Num3:
        letra=Alfabeto[num]
        Encriptado.append(letra)
    if EspacioF!=[]:
        for i in range(len(EspacioF)):
            E=EspacioF[i]
            Encriptado.insert(E," ")
    Respuesta="".join(Encriptado)
    return Respuesta

def DecodvVigenere(mfra3,mcla3):
    Alfabeto =("abcdefghijklmnñopqrstuvwxyz")
    Num1=[]
    EspacioCrip=[]
    ECrip=mfra3.find(" ")
    EspacioClaCri=[]
    EClaC=mcla3.find(" ")

    Num1=[]
    for letra in mfra3:
        if letra in Alfabeto:
            X=Alfabeto.find(letra)
            Num1.append(X)
    while ECrip!=-1:
        EspacioCrip.append(ECrip)
        ECrip=mfra3.find(" ",ECrip+1)

    Num2=[]
    while len(Num1)>len(Num2): 
        for letra in mcla3:
            if letra in Alfabeto:
                X=Alfabeto.find(letra)
                Num2.append(X)
            else:
                if letra==" ":  
                    EspacioClaCri.append(EClaC.index(letra))
    while EClaC!=-1:
        EspacioClaCri.append(EClaC)
        EClaC=mcla3.find(" ",EClaC+1)

    Num3=[]
    for a, b in zip(Num1, Num2):
        R=a-b
        if R<0:
            R=27-abs(R)
            Num3.append((R))
        else:
            Num3.append((R))

    Decodificar=[]
    for num in Num3:
        letra=Alfabeto[num]
        Decodificar.append(letra)
    if EspacioCrip!=[]:
        for i in range(len(EspacioCrip)):
            E=EspacioCrip[i]
            Decodificar.insert(E," ")
    Respuesta="".join(Decodificar)
    return Respuesta

#Menu de bienvenida
print("\n Bienvenidos a nuestro programa de encriptado, aqui podran encontrar los siguientes\n Tipos de encriptacion:\n\n\t1.Cifrado César\n\t\tSustituye cada letra del texto por otra que se encuentre un\n\t\t numero indicado de posciones adelante del original en el alfabeto\n\n\t2.Cifrado monoalfabético\n\t\t Toma el texto y una clave, coloca todas las letras de la clave que\n\t\t no se repiten al inico del alfabeto, lo que cambia la posicion original de cada letra, \n\t\tsustituye cada letra del texto por la nueva letra que se encuentra en la nueva posicion\n\n\t3.Cifrado Vigenère\n\t\t Toma el texto y clave, utiliza el valor de las letras de la clave para que por formula\n\t\t de una posicion en el alfabeto y remplace cada letra del texto por la letra \n\t\tdel resultado de la formula \n\t")
print()
print("Equipo #3\n Integrantes:\n\t Abigail Jimenez Mata \n\t Kamila Rachelle Chacon Morales \n\t Daniel Andres Ceciliano Calderon") 
print()     
print("Este es el alfabeto que se utiliza para realizar la encriptacion: \n\tabcdefghijklmnñopqrstuvwxyz")
print()
Frase=str(input("Ingrese la frase,no puede ser vacio: \n\t"))
print()
print("Frase ingresada: ",Frase)
mfra1=SinTD(Frase)
mfra2=depurar(mfra1)
mfra3=Minus(mfra2)
print("Frase transformada: ",mfra3)
mfra=0
#Menu de funciones
Menu=True
Menu0=False
while Menu==True:
    if Menu0==True:
        print("Programa Reiniciado\n")
        Frase=str(input("Ingrese la anterior frase o una nueva,no puede ser vacio: \n\t"))
        print()
        print("Frase ingresada: ",Frase)
        mfra1=SinTD(Frase)
        mfra2=depurar(mfra1)
        mfra3=Minus(mfra2)
        print("Frase transformada: ",mfra3)
        Menu0=False
    else:
        Menu1=True
        Menu2=True
        op=(input("¿Que desea hacer con la frase?\n\t 1.Codificar\n\t 2.Decodificar \n\t 3.Cancelar \n\t"))
        if op=="1":
            while Menu1==True:
                Menu2=True
                op2=(input("Ingrese la cantidad de tecnicas que desea realizar (de 1 a 3) o 4 para Cancelar \n\t"))
                if op2=="1":
                    while Menu2==True:
                        op3=(input("Cual desea utilizar: \n\t1.César\n\t2.Monoalfabético\n\t3.Vigénere\n\t4.Cancelar \n\t"))
                        if op3=="1":
                            print("César")
                            """ 




                            """
                        elif op3=="2":
                            print("Monoalfabético")
                            """ 




                            """
                        elif op3=="3":
                            print("Vigénere")
                            Clave=input("Ingrese la palabra clave para codificar: \n\t")
                            mcla1=SinTD(Clave)
                            mcla2=depurar(mcla1)
                            mcla3=Minus(mcla2)
                            Encriptado=CodiVigenere(mfra3,mcla3)
                            print("Palabra original: ",mfra3)
                            print("Palabra encriptada: ",Encriptado)
                            print()
                            T=input("¿Desea continuar utilizando el programa?\n\t 1.Si\n\t 2.No\n\t")
                            if T=="1":
                                Menu0=True
                                Menu1=False
                                Menu2=False
                            elif T=="2":
                                Menu1=False
                                Menu2=False
                                Menu=False
                            else:
                                print("Ingrese una opción válida")

                        elif op3=="4":
                            T=(input("¿Desea volver al menu anterior?\n\t1.Si\n\t2.No\n\t3.Continuar\n\t"))
                            if T=="1":
                                Menu2=False
                        elif T=="2":
                            T=(input("¿Desea finalizar el programa?\n\t1.Si\n\t2.No\n\t"))
                            if T=="1":
                                Menu2=False
                                Menu1=False
                                Menu=False
                            elif T=="2":
                                Menu0=True
                                print()
                            else:
                                print("Ingrese una opción válida")
                        elif T=="3":
                            print()
                        else:
                            print("Ingrese una opción válida")


                elif op2=="2":
                    while Menu2==True:
                        op3=(input("Cuales 2 tecnicas desea utilizar (Indique la primera y segunda por separado): \n\t1.César\n\t2.Monoalfabético\n\t3.Vigénere\n\t4.Cancelar\n\t"))
                        op32=(input())
                        if op3=="4" or op32=="4":
                            T=(input("¿Desea volver al menu anterior?\n\t1.Si\n\t2.No\n\t3.Continuar\n\t"))
                            if T=="1":
                                    Menu2=False
                            elif T=="2":
                                T=(input("¿Desea finalizar el programa?\n\t1.Si\n\t2.No\n\t"))
                                if T=="1":
                                    Menu2=False
                                    Menu1=False
                                    Menu=False
                                elif T=="2":
                                    Menu0=True
                                    print()
                                else:
                                    print("Ingrese una opción válida")
                            elif T=="3":
                                print()
                            else:
                                print("Ingrese una opción válida")


                elif op2=="3":
                    while Menu2==True:
                        op3=(input("Ingrese el orden que desea utilizar, 1 a la vez: \n\t1.César\n\t2.Monoalfabético\n\t3.Vigénere\n\t4.Cancelar\n\t"))
                        op32=(input())
                        op33=(input())

                        if op3=="4" or op32=="4" or op33=="4":
                            T=(input("¿Desea volver al menu anterior?\n\t1.Si\n\t2.No\n\t3.Continuar\n\t"))
                            if T=="1":
                                    Menu2=False
                            elif T=="2":
                                T=(input("¿Desea finalizar el programa?\n\t1.Si\n\t2.No\n\t"))
                                if T=="1":
                                    Menu0=True
                                    Menu2=False
                                    Menu1=False
                                    Menu=False
                                elif T=="2":
                                    print()
                                else:
                                    print("Ingrese una opción válida")
                            elif T=="3":
                                print()
                            else:
                                print("Ingrese una opción válida")


                elif op2=="4":
                    T=(input("¿Desea volver al menu anterior?\n\t1.Si\n\t2.No\n\t3.Continuar\n\t"))
                    if T=="1":
                        Menu1=False
                    elif T=="2":
                        T=(input("¿Desea finalizar el programa?\n\t1.Si\n\t2.No\n\t"))
                        if T=="1":
                            Menu2=False
                            Menu1=False
                            Menu=False
                        elif T=="2":
                            Menu0=True
                            print()
                        else:
                            print("Ingrese una opción válida")
                    else:
                        print("Ingrese una opción válida")
                else:
                    print("Ingrese una opción válida")






        elif op=="2":
            print("Decodificar")
            while Menu2==True:
                op3=(input("Cual desea utilizar: \n\t1.César\n\t2.Monoalfabético\n\t3.Vigénere\n\t4.Cancelar \n\t"))
                if op3=="1":
                    print("César")
                    """ 




                    """
                elif op3=="2":
                    print("Monoalfabético")
                    """ 




                    """
                elif op3=="3":
                    print("Vigénere")
                    Clave=input("Ingrese la palabra clave para Decodificar: \n\t")
                    mcla1=SinTD(Clave)
                    mcla2=depurar(mcla1)
                    mcla3=Minus(mcla2)
                    Decodificar=DecodvVigenere(mfra3,mcla3)
                    print("Palabra original encriptada: ",mfra3)
                    print("Palabra desencriptada: ",Decodificar)
                    print()
                    T=input("¿Desea continuar utilizando el programa?\n\t 1.Si\n\t 2.No\n\t")
                    if T=="1":
                        Menu0=True
                        Menu1=False
                        Menu2=False
                    elif T=="2":
                        Menu1=False
                        Menu2=False
                        Menu=False
                    else:
                        print("Ingrese una opción válida")

                elif op3=="4":
                    T=(input("¿Desea volver al menu anterior?\n\t1.Si\n\t2.No\n\t3.Continuar\n\t"))
                    if T=="1":
                        Menu2=False
                    elif T=="2":
                        T=(input("¿Desea finalizar el programa?\n\t1.Si\n\t2.No\n\t"))
                        if T=="1":
                            Menu2=False
                            Menu1=False
                            Menu=False
                        elif T=="2":
                            Menu0=True
                            print()
                        else:
                                print("Ingrese una opción válida")
                    elif T=="3":
                        print()
                    else:
                        print("Ingrese una opción válida")        



        elif op=="3":
            T=(input("¿Desea finalizar el programa?\n\t1.Si\n\t2.No\n\t"))
            if T=="1":
                Menu=False
            if T=="2":
                Menu0=True
                print()
            else:
                print("Ingrese una opción válida")
        else:
                print("Ingrese una opción válida")
    print("\n\nPrograma Finalizado")

                  

