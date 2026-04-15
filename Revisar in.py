#DEPURAR LA FRASE


#Descripcion: Recibe la frase o palabra que ingrese el usuario y remueve todo tipo de tilde, dierecis, etc... que se encuentren en las vocales
#Entrada: Recibe la palabra o frase tenga o no tildes o dierecis
#Salida: Devuelve la frase o palabra sin las tildes o dierecis que tenia la original
#restricciones: N/A
def VSINTD (Palabra):
    ReemplazoA=[# A
        "á","à","â","ä","ã","å","ā","ă","ą","Á","À","Â","Ä","Ã","Å","Ā","Ă","Ą", ]
    ReemplazoE=[# E
        "é","è","ê","ë","ē","ĕ","ė","ę","ě","É","È","Ê","Ë","Ē","Ĕ","Ė","Ę","Ě"]
    ReemplazoI=[# I
        "í","ì","î","ï","ī","ĭ","į","ı","Í","Ì","Î","Ï","Ī","Ĭ","Į"]
    ReemplazoO=[# O
        "ó","ò","ô","ö","õ","ø","ō","ŏ","ő","Ó","Ò","Ô","Ö","Õ","Ø","Ō","Ŏ","Ő"]
    ReemplazoU=[# U
        "ú","ù","û","ü","ū","ŭ","ů","ű","ų","Ú","Ù","Û","Ü","Ū","Ŭ","Ů","Ű","Ų"]
    Resultado=""
    for Letra in Palabra:
        if Letra in ReemplazoA:
            Resultado+="a"
        elif Letra in ReemplazoE:
            Resultado+="e"
        elif Letra in ReemplazoI:    
            Resultado+="i"
        elif Letra in ReemplazoO:              
            Resultado+="o"
        elif Letra in ReemplazoU:
            Resultado+="u"
        else:                         
            Resultado+=Letra
    return Resultado

#Descripcion: Recibe la frase o palabra que deja la funcion SinTD y remueve todo tipo de simbolo o valor que no este en el albabeto mayuscula o miniscula
#Entrada: Recibe la palabra o frase sin tildes o dierecis
#Salida: Devuelve la frase o palabra solo con las letras y espacios que contenia originalmente
#restricciones: N/A
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

#Descripcion: Recibe la frase o palabra que devuelve la funcion Depurar y convierte todo en minúsculas
#Entrada: Recibe la palabra o frase solo con letras mayúsculas, minúsculas y espacios
#Salida: Devuelve la frase o palabra solo con minusculas y espacios
#restricciones: N/A
def Minus(F):
    m=F.lower()
    return m

def Vacio(mfra3):
    re=False
    print("\n¡¡¡ADVERTENCIA!!!\n\n La frase transformada no posee ninguna letra\n por lo que el programa no podra devolver un valor\n\n Si desea reiniciar el programa, ingrese 1\n\n Si desea cancelar programa Ingrese 2\n\n")
    while re==False:
        OP=input()
        if OP== "1":
            Frase = input("Ingrese la frase anterior corregida o una nueva: \n\t")
            mfra1 = VSINTD(Frase)
            mfra2 = depurar(mfra1)
            mfra3 = Minus(mfra2)
            print("Frase transformada:", mfra3)
            if Frase=="":
                while Frase =="":
                    Frase = input("El valor de la frase no puede ser vacío: \n\t")
                    print("Frase ingresada:", Frase)
                    mfra1 = VSINTD(Frase)
                    mfra2 = depurar(mfra1)
                    mfra3 = Minus(mfra2)
                    print("Frase transformada:", mfra3)
                if mfra3 == "":
                    while mfra3=="":
                        print("Frase ingresada:", Frase)
                        print("Frase transformada:", mfra3)
                        print("\nLa frase transformada sigue vacía. Intente otra vez.")
                        Frase = input()
                        mfra1 = VSINTD(Frase)
                        mfra2 = depurar(mfra1)
                        mfra3 = Minus(mfra2)
                        print("Frase transformada:", mfra3)
                    return mfra3
                else:
                    return mfra3
            if mfra3=="":
                while mfra3=="":
                            print("Frase ingresada:", Frase)
                            print("Frase transformada:", mfra3)
                            print("\nLa frase transformada sigue vacía. Intente otra vez.")
                            Frase = input()
                            mfra1 = VSINTD(Frase)
                            mfra2 = depurar(mfra1)
                            mfra3 = Minus(mfra2)
                            print("Frase transformada:", mfra3)
                return mfra3
            else:
                    return mfra3
        elif OP=="2":
            Menu=False
            re=True
            return Menu
        else:
            print("ingrese un valor valido")
    mfra1 = VSINTD(Frase)
    mfra2 = depurar(mfra1)
    mfra3 = Minus(mfra2)
    print("Frase transformada:", mfra3)
    return mfra3
#CODIFICACIÓN VIGENERE

#Descripcion: Recibe la frase resultante de las funciones anteriores, la palabra clave, y procede a codificar la frase
#Entrada: Recibe la palabra clave y la frase transformada ingresada anteriormente 
#Salida: Devuelve la frase con la encriptacion Vigenère
#restricciones: N/A
def CodiVigenere(frase, clave):
    if clave == "":
        while clave=="":
            clave=str(input("La clave no puede ser un valor vacio: \n\t"))
    Alfabeto =("abcdefghijklmnñopqrstuvwxyz")
    EspacioF=[]
    EF=frase.find(" ")
    EspacioC=[]
    EC=clave.find(" ")

    Num1=[]
    for letra in frase:
        if letra in Alfabeto:
            X=Alfabeto.find(letra)
            Num1.append(X)
    while EF!=-1:
        EspacioF.append(EF)
        EF=frase.find(" ",EF+1)

    Num2=[]
    while len(Num1)>len(Num2): 
        for letra in clave:
            if letra in Alfabeto:
                X=Alfabeto.find(letra)
                Num2.append(X)
            else:
                if letra==" ":  
                    EspacioC.append(clave.index(letra))
    while EC!=-1:
        EspacioC.append(EC)
        EC=clave.find(" ",EC+1)


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

#DECODIFICACIÓN VIGENERE

#Descripcion: Recibe la frase codificada y la palabra clave, y procede a decodificar la frase
#Entrada: Recibe la palabra clave y la frase codificada ingresada anteriormente 
#Salida: Devuelve la frase encriptada con la encriptacion Vigenère desencriptada
#restricciones: N/A
def DecodvVigenere(frase,clave):
    if clave == "":
        while clave=="":
            clave=str(input("La clave no puede ser un valor vacio: \n\t"))
    Alfabeto =("abcdefghijklmnñopqrstuvwxyz")
    Num1=[]
    EspacioCrip=[]
    ECrip=frase.find(" ") #A Ecript se le podría poner otro nombre como fraseEcriptada o no se :)
    EspacioClaCri=[]
    EClaC=clave.find(" ") # A este tambien 

    Num1=[]
    for letra in mfra3:
        if letra in Alfabeto:
            X=Alfabeto.find(letra)
            Num1.append(X)
    while ECrip!=-1:
        EspacioCrip.append(ECrip)
        ECrip=frase.find(" ",ECrip+1)

    Num2=[]
    while len(Num1)>len(Num2): 
        for letra in clave:
            if letra in Alfabeto:
                X=Alfabeto.find(letra)
                Num2.append(X)
            else:
                if letra==" ":  
                    EspacioClaCri.append(EClaC.index(letra))
    while EClaC!=-1:
        EspacioClaCri.append(EClaC)
        EClaC=clave.find(" ",EClaC+1)

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
            E=EspacioCrip[i] #A E tambien se le deberia cambiar el nombre
            Decodificar.insert(E," ")
    Respuesta="".join(Decodificar)
    return Respuesta

#MENÚ DE BIENVENIDA

print("\n Bienvenidos a nuestro programa de encriptado, aqui podran encontrar los siguientes\n Tipos de encriptacion:\n\n\t1.Cifrado César\n\t\tSustituye cada letra del texto por otra que se encuentre un\n\t\t numero indicado de posciones adelante del original en el alfabeto\n\n\t2.Cifrado monoalfabético\n\t\t Toma el texto y una clave, coloca todas las letras de la clave que\n\t\t no se repiten y las coloca al inico del alfabeto, cambiando la posicion original de cada letra, \n\t\tsustituye cada letra del texto por la nueva letra que se encuentra en la nueva posicion\n\n\t3.Cifrado Vigenère\n\t\t Toma el texto y la clave, utiliza el valor de las letras de la clave para que por formula\n\t\t de una posicion en el alfabeto y remplace cada letra del texto por la letra \n\t\tdel resultado de la formula \n\t")
print()
print("Equipo #3\n Integrantes:\n\t Abigail Jimenez Mata \n\t Kamila Chacón Morales \n\t Daniel Andres Ceciliano Calderon") 
print()     
print("Este es el alfabeto que se utiliza para realizar la encriptacion: \n\tabcdefghijklmnñopqrstuvwxyz")
print()
Frase=str(input("Ingrese la frase,no puede ser vacio: \n\t"))
if Frase=="":
    while Frase=="":
        Frase=str(input("El valor de la frase no puede ser vacio: \n\t"))
else:
    print()
    print("Frase ingresada: ",Frase)
    mfra1=VSINTD(Frase)
    mfra2=depurar(mfra1)
    mfra3=Minus(mfra2)
    print("Frase transformada: ",mfra3)
    while mfra3=="":
        mfra3=Vacio(mfra3)
        if mfra3==False:
            print("Programa finalizado")
            Menu=False

    #MENÚ DE INVOCACION DE FUNCIONES
    Menu=True
    Menu0=False
    while Menu==True:
        if Menu0==True:
            while Menu0==True:
                """Esta se activa en caso de que el usuario reinicie el programa"""

                print("Programa Reiniciado\n")
                Frase=str(input("Ingrese la frase anterior o una nueva,no puede ser vacio: \n\t"))
                print()
                if Frase=="":
                    while Frase=="":
                        Frase=str(input("El valor de la frase no puede ser vacio: \n\t"))
                else:
                    print("Frase ingresada: ",Frase)
                    mfra1=VSINTD(Frase)
                    mfra2=depurar(mfra1)
                    mfra3=Minus(mfra2)
                    print("Frase transformada: ",mfra3)
                    while mfra3=="":
                        mfra3=Vacio(mfra3)
                        if mfra3==False:
                            Menu=False
                    Menu0=False
        else:
            Menu1=True
            Menu2=True
            op=(input("¿Que desea hacer con la frase?\n\t 1.Codificar\n\t 2.Decodificar \n\t 3.Cancelar \n\t"))
            if op=="1":
                """ MENU PARA CODIFICAR """

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
    #OTRAS OPCIONES

                                """
                            elif op3=="3":
                                print("Vigénere")
                                Clave=input("Ingrese la palabra clave para codificar: \n\t")
                                mcla1=VSINTD(Clave)
                                mcla2=depurar(mcla1)
                                mcla3=Minus(mcla2)
                                Encriptado=CodiVigenere(mfra3,mcla3)
                                if Encriptado=="":
                                    print("\n No fue posible realizar la encriptacion debido que la frase ingresada\n NO poseia ningun tipo de letra")
                                else:
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
                            else:
                                print("Ingrese una opción válida")

    #INVOCACION DE DOS TECNICAS

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

    #INVOCACIÓN DE TRES TECNICAS

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
                                    print("Ingrese una opción válida para continuar")


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


    #MENÚ DE INVOCACIÓN DE FUNCIONES DECODIFICADORAS

    #DECODIFICACIÓN CESAR

            elif op=="2":
                """ MENU PARA DECODIFICAR """

                print("Decodificar")
                while Menu2==True:
                    op3=(input("Cual desea utilizar: \n\t1.César\n\t2.Monoalfabético\n\t3.Vigénere\n\t4.Cancelar \n\t"))
                    if op3=="1":
                        print("César")
                        """ 


    #DECODIFICACIÓN MONOALFABÉTICO

                        """
                    elif op3=="2":
                        print("Monoalfabético")
                        """ 



    #DECODIFICACIÓN VIGENERE

                        """
                    elif op3=="3":
                        print("Vigénere")
                        Clave=input("Ingrese la palabra clave para Decodificar: \n\t")
                        mcla1=VSINTD(Clave)
                        mcla2=depurar(mcla1)
                        mcla3=Minus(mcla2)
                        Decodificar=DecodvVigenere(mfra3,mcla3)
                        if Decodificar=="":
                            print( "\n No fue posible realizar la desencriptacion debido a que la frase ingresada\n NO poseia ningun tipo de letra")
                        else:
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

    #OTRAS OPCIONES

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
                """ MENU PARA CERRAR EL PROGRAMA DESDE EL INICIO  O RETOMARLO """
                
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
    if Menu==False:
        print("Programa finalizado")

#prueba de Kami