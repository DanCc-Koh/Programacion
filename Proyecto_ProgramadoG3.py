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

#DEPURAR LA FRASE
""" Cod Cesar"""

#Descripción:
#Entradas:
#Salidas:
#Restricciones:
def Vacio(mfra3):
    re=False
    while re==False:
        print("\n¡¡¡ADVERTENCIA!!!\n\n La frase transformada no posee ninguna letra\n por lo que el programa no podra devolver un valor\n\n Si desea reiniciar el programa, ingrese 1\n\n Si desea cancelar programa Ingrese 2\n\n")
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

#Descripción: Codifica una frase usando el cifrado César. 
#Entrada: frase textual, número desplazamiento
#Salida: Texto codificado ó vacío
#Restricciones: Alfabeto de 27 letras (se incluye la ñ)
def CodCesar(frase, desplazamiento):
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    if frase == "" or frase == None: 
        return ""
    frase_codificada = ""
    for i in range(len(frase)):
        let_Act = frase[i]
        if let_Act == " ":
            frase_codificada = frase_codificada + " "
        else:
            letra_min = let_Act.lower()
            if letra_min in alfabeto:
                pos_a = -1
                contador = 0
                while contador < len(alfabeto):
                    if alfabeto[contador] == letra_min:
                        pos_a = contador
                    contador = contador + 1
                new_pos = pos_a + desplazamiento
                while new_pos > 26:
                    new_pos = new_pos - 27
                while new_pos < 0:
                    new_pos = new_pos + 27
                let_fin = alfabeto[new_pos]
                frase_codificada = frase_codificada + let_fin
    return frase_codificada

#Descripción: Decodifica una frase textual utilizando el método de César al inverso.
#Entrada: frase textual codificada, número desplazamiento
#Salida: Texto original
#Restricciones: desplazamiento entero

def DecodCesar(frase, desplazamiento):
    if frase == " ":
        return " "
    desplazamiento_inv = desplazamiento * -1
    resul_02 = CodCesar(frase, desplazamiento_inv)
    return resul_02
""" Cod Cesar"""



""" Cod Monoalfabetico """
#Descripción:
#Entradas:
#Salidas:
#Restricciones:
def depurarClave(claveOriginal):
    if claveOriginal=="": 
        mcla5=True  
        while mcla5==True:
            claveOriginal=str(input("La clave no puede ser un valor vacio: \n\t"))
            mcla1=VSINTD(claveOriginal)
            mcla2=depurar(mcla1)
            mcla4=Minus(mcla2)
            if mcla4!="":
                mcla5=False
        claveNueva = "" #texto vacio para ir creando la clave depurada poco a poco
        for x in claveOriginal: 
            if x not in claveNueva: #Si la letra en la clave original no se ha guardado ya en la clave nueva entonces se guarda en la variable
                claveNueva += x
        return claveNueva
    else:
        claveNueva = "" #texto vacio para ir creando la clave depurada poco a poco
        for x in claveOriginal: 
            if x not in claveNueva: #Si la letra en la clave original no se ha guardado ya en la clave nueva entonces se guarda en la variable
                claveNueva += x
        return claveNueva

#Descripción:
#Entradas:
#Salidas:
#Restricciones:
def depurarAbecedario(claveNueva):
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    resultado1 = "" #texto vacio para construir de a poco el abecedario nuevo
    resultado2 = "" #texto vacio para guardar la union

    for x in abecedario:
        if x not in claveNueva: #si la letra del abecedario no está en la clave entonces se guarda en resultado
            resultado1 += x
            resultado2 = claveNueva + resultado1
    return resultado2

#Descripción:
#Entradas:
#Salidas:
#Restricciones:
def monoalfabetico(texto, claveOriginal):
    abecedario = "abcdefghijklmnñopqrstuvwxyz" #abecedario original
    claveNueva = depurarClave(claveOriginal) #clave depurada para que la use la funcion de abecedario nuevo
    abecedarioNuevo = depurarAbecedario(claveNueva) #abecedario nuevo
    resultado = "" #string vacio para guardar el resultado final

    for x in texto: #para cada letra en el texto que sea un espacio se guarda el resultado y queda igual
        if x == " ":
            resultado += " "
        else:
            posicion = abecedario.find(x) #busca la posición de la letra en el abecedario original
            resultado += abecedarioNuevo[posicion] #se usa la posicion del numero en el abecedario nuevo y se guarda en resultado
    return resultado

#Descripción:
#Entradas:
#Salidas:
#Restricciones:
def decodificacionMono(textoCifrado, clave): 
    abecedario2 = "abcdefghijklmnñopqrstuvwxyz" #abecedario nuevo
    claveDepurada = depurarClave(clave) #clave depurada
    abecedario1 = depurarAbecedario(claveDepurada) #abecedario original
    
    resultado = ""

    for x in textoCifrado: #agarra el texto cifrado y si la letra es un espacio lo deja igual 
        if x == " ":
            resultado += " "
        else:
            posicion = abecedario1.find(x) #sino busca su posicion en el abecedario nuevo y la sustiyuye
            resultado += abecedario2[posicion]
    return resultado


""" Cod Monoalfabetico """


#CODIFICACIÓN VIGENERE

#Descripcion: Recibe la frase resultante de las funciones anteriores, la palabra clave, y procede a codificar la frase
#Entrada: Recibe la palabra clave y la frase transformada ingresada anteriormente 
#Salida: Devuelve la frase con la encriptacion Vigenère
#restricciones: N/A
def CodiVigenere(frase, clave):
    if clave == "":
        mfra4=""
        while mfra4=="":
                clave=str(input("La clave no puede ser un valor vacio: \n\t"))
                mcla1=VSINTD(clave)
                mcla2=depurar(mcla1)
                mcla4=Minus(mcla2)

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

#
#
#
#
def canfun2(op3,op32):
    global mfra3
    Cesar="1"
    Monosi="2"
    Vigenere="3"
    ok1=True
    while ok1==True:
        if op3==Cesar:
            try:
                desplazamiento = int(input("Ingrese la cantidad de posiciones a desplazar (ejemplo 3): "))
                Encrip_Cesar = CodCesar(mfra3, desplazamiento)
                print()
                mfra3=Encrip_Cesar
                ok1=False
            except ValueError:
                print("ERROR: Debe ingresar un número entero para el desplazamiento")
                print()
                desplazamiento = int(input("Ingrese la cantidad de posiciones a desplazar (ejemplo 3): "))
            ok1=False

        elif op3==Monosi:
            clave=input("Ingrese la palabra clave para codificar (Para Monoalfabetico): \n\t")
            mfra1=VSINTD(clave)
            mfra2=depurar(mfra1)
            mfra4=Minus(mfra2)
            cifrado=monoalfabetico(mfra3, mfra4)
            mfra3=cifrado
            print()

            ok1=False

        elif op3==Vigenere:
            Clave=input("Ingrese la palabra clave para codificar (Para Vigenere): \n\t")
            mcla1=VSINTD(Clave)
            mcla2=depurar(mcla1)
            mcla3=Minus(mcla2)
            Encriptado=CodiVigenere(mfra3,mcla3)
            if Encriptado=="":
                print("\n No fue posible realizar la encriptacion debido que la frase ingresada\n NO poseia ningun tipo de letra")
            else:
                mfra3=Encriptado
                ok1=False
                print()
        else:
            print("Opcion no valida,\n\t1.César\n\t2.Monoalfabético\n\t3.Vigénere")
            op3=input()

    ok2=True
    while ok2==True:
        if op32==Cesar:
            try:
                desplazamiento = int(input("Ingrese la cantidad de posiciones a desplazar (ejemplo 3): "))
                Encrip_Cesar = CodCesar(mfra3, desplazamiento)
                print("Palabra encriptada (César): ", Encrip_Cesar)
                print()
            except ValueError:
                print("ERROR: Debe ingresar un número entero para el desplazamiento")
                print()
                desplazamiento = int(input("Ingrese la cantidad de posiciones a desplazar (ejemplo 3): "))
            ok2=False

        elif op32==Monosi:
            clave=input("Ingrese la palabra clave para codificar (Para Monoalfabetico): \n\t")
            mfra1=VSINTD(clave)
            mfra2=depurar(mfra1)
            mfra4=Minus(mfra2)
            cifrado=monoalfabetico(mfra3, mfra4)
            print("Texto encriptada: ",cifrado)
            print()
            ok2=False
        elif op32==Vigenere:
            Clave=input("Ingrese la palabra clave para codificar (Para Vigenere): \n\t")
            mcla1=VSINTD(Clave)
            mcla2=depurar(mcla1)
            mcla3=Minus(mcla2)
            Encriptado=CodiVigenere(mfra3,mcla3)
            if Encriptado=="":
                print("\n No fue posible realizar la encriptacion debido que la frase ingresada\n NO poseia ningun tipo de letra")
            else:
                print("Palabra encriptada: ",Encriptado)
            ok2=False
            print()
        else:
            print("Opcion no valida,\n\t1.César\n\t2.Monoalfabético\n\t3.Vigénere")
            op32=input()
    return

#
#
#
#
def canfun3(op3,op32,op33):
    global mfra3
    Cesar="1"
    Monosi="2"
    Vigenere="3"
    ok1=True
    while ok1==True:
        if op3==Cesar:
            try:
                desplazamiento = int(input("Ingrese la cantidad de posiciones a desplazar (ejemplo 3): "))
                Encrip_Cesar = CodCesar(mfra3, desplazamiento)
                print()
                mfra3=Encrip_Cesar
                ok1=False
            except ValueError:
                print("ERROR: Debe ingresar un número entero para el desplazamiento")
                print()
                desplazamiento = int(input("Ingrese la cantidad de posiciones a desplazar (ejemplo 3): "))
            ok1=False

        elif op3==Monosi:
            clave=input("Ingrese la palabra clave para codificar (Para Monoalfabetico): \n\t")
            mfra1=VSINTD(clave)
            mfra2=depurar(mfra1)
            mfra4=Minus(mfra2)
            cifrado=monoalfabetico(mfra3, mfra4)
            mfra3=cifrado
            print()

            ok1=False

        elif op3==Vigenere:
            Clave=input("Ingrese la palabra clave para codificar (Para Vigenere): \n\t")
            mcla1=VSINTD(Clave)
            mcla2=depurar(mcla1)
            mcla3=Minus(mcla2)
            Encriptado=CodiVigenere(mfra3,mcla3)
            if Encriptado=="":
                print("\n No fue posible realizar la encriptacion debido que la frase ingresada\n NO poseia ningun tipo de letra")
            else:
                mfra3=Encriptado
                ok1=False
                print()
        else:
            print("Opcion no valida,\n\t1.César\n\t2.Monoalfabético\n\t3.Vigénere")
            op3=input()


    ok2=True
    while ok2==True:
        if op32==Cesar:
            try:
                desplazamiento = int(input("Ingrese la cantidad de posiciones a desplazar (ejemplo 3): "))
                Encrip_Cesar = CodCesar(mfra3, desplazamiento)
                print()
                mfra3=Encrip_Cesar
                ok2=False
            except ValueError:
                print("ERROR: Debe ingresar un número entero para el desplazamiento")
                print()
                desplazamiento = int(input("Ingrese la cantidad de posiciones a desplazar (ejemplo 3): "))
            ok2=False

        elif op32==Monosi:
            clave=input("Ingrese la palabra clave para codificar (Para Monoalfabetico): \n\t")
            mfra1=VSINTD(clave)
            mfra2=depurar(mfra1)
            mfra4=Minus(mfra2)
            cifrado=monoalfabetico(mfra3, mfra4)
            mfra3=cifrado
            print()

            ok2=False

        elif op32==Vigenere:
            Clave=input("Ingrese la palabra clave para codificar (Para Vigenere): \n\t")
            mcla1=VSINTD(Clave)
            mcla2=depurar(mcla1)
            mcla3=Minus(mcla2)
            Encriptado=CodiVigenere(mfra3,mcla3)
            if Encriptado=="":
                print("\n No fue posible realizar la encriptacion debido que la frase ingresada\n NO poseia ningun tipo de letra")
            else:
                mfra3=Encriptado
                ok2=False
                print()
        else:
            print("Opcion no valida,\n\t1.César\n\t2.Monoalfabético\n\t3.Vigénere")
            op3=input()


    ok3=True
    while ok3==True:
        if op33==Cesar:
            try:
                desplazamiento = int(input("Ingrese la cantidad de posiciones a desplazar (ejemplo 3): "))
                Encrip_Cesar = CodCesar(mfra3, desplazamiento)
                print("Palabra encriptada (César): ", Encrip_Cesar)
                print()
            except ValueError:
                print("ERROR: Debe ingresar un número entero para el desplazamiento")
                print()
                desplazamiento = int(input("Ingrese la cantidad de posiciones a desplazar (ejemplo 3): "))
            ok3=False

        elif op33==Monosi:
            clave=input("Ingrese la palabra clave para codificar (Para Monoalfabetico): \n\t")
            mfra1=VSINTD(clave)
            mfra2=depurar(mfra1)
            mfra4=Minus(mfra2)
            cifrado=monoalfabetico(mfra3, mfra4)
            print("Texto encriptada: ",cifrado)
            print()
            ok3=False
        elif op33==Vigenere:
            Clave=input("Ingrese la palabra clave para codificar (Para Vigenere): \n\t")
            mcla1=VSINTD(Clave)
            mcla2=depurar(mcla1)
            mcla3=Minus(mcla2)
            Encriptado=CodiVigenere(mfra3,mcla3)
            if Encriptado=="":
                print("\n No fue posible realizar la encriptacion debido que la frase ingresada\n NO poseia ningun tipo de letra")
            else:
                print("Palabra encriptada: ",Encriptado)
            ok3=False
            print()
        else:
            print("Opcion no valida,\n\t1.César\n\t2.Monoalfabético\n\t3.Vigénere")
            op32=input()
    return







#MENÚ DE BIENVENIDA
Menu=True
Menu0=False
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
            Menu=False

    #MENÚ DE INVOCACION DE FUNCIONES
    while Menu==True:
        if Menu0==True:
            while Menu0==True:
                """Esta se activa en caso de que el usuario reinicie el programa"""

                print("Programa Reiniciado\n")
                Frase=str(input("Ingrese la frase anterior o una nueva,no puede ser vacio: \n\t"))
                print()
                if Frase=="":
                    while mfra3=="":
                        Frase=str(input("El valor de la frase no puede ser vacio: \n\t"))
                        mfra1=VSINTD(Frase)
                        mfra2=depurar(mfra1)
                        mfra3=Minus(mfra2)
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
                mfra1=VSINTD(Frase)
                mfra2=depurar(mfra1)
                mfra3=Minus(mfra2)
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
                                try:
                                    print("César")
                                    desplazamiento = int(input("Ingrese la cantidad de posiciones a desplazar (ejemplo 3): "))
                                    Encrip_Cesar = CodCesar(mfra3, desplazamiento)
                                    print("\n Palabra original: ", mfra3)
                                    print("Palabra encriptada (César): ", Encrip_Cesar)
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
                                except ValueError:
                                    print("ERROR: Debe ingresar un número entero para el desplazamiento")
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



                            elif op3=="2":
                                print("Monoalfabético")
                                clave=input("Ingrese la palabra clave para codificar: \n\t")
                                mfra1=VSINTD(clave)
                                mfra2=depurar(mfra1)
                                mfra4=Minus(mfra2)
                                cifrado=monoalfabetico(mfra3, mfra4)
                                print("Texto original: ",mfra3)
                                print("Texto encriptada: ",cifrado)
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
                            op32=(input("\n\t"))
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
                            elif op3=="1" or op32=="1" or op3=="2" or op32=="2" or op3=="3" or op32=="3":
                                canfun2(op3,op32)
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
                            else:
                                print("opciones no validas")
                                

    #INVOCACIÓN DE TRES TECNICAS

                    elif op2=="3":
                        while Menu2==True:
                            op3=(input("Ingrese el orden que desea utilizar, 1 a la vez: \n\t1.César\n\t2.Monoalfabético\n\t3.Vigénere\n\t4.Cancelar\n\t"))
                            op32=(input("\n\t"))
                            op33=(input("\n\t"))
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
                            elif op3=="1" or op32=="1" or op33=="1" or op3=="2" or op32=="2" or op33=="2" or op3=="3" or op32=="3" or op33=="3":
                                canfun3(op3,op32,op33)
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
                            else:
                                print("opciones no validas")


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
                        try:
                            desplazamiento = int(input("Ingrese el número de desplazamiento original: "))
                            DecodCesar = DecodCesar(mfra3, desplazamiento)
                            print("\n Palabra original encriptada: ", mfra3)
                            print("Palabra desencriptada: ", DecodCesar)
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
                        except ValueError:
                            print("ERROR: El desplazamiento debe ser en un número entero.")
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


    #DECODIFICACIÓN MONOALFABÉTICO

                    
                    elif op3=="2":
                        print("Monoalfabético")
                        clave=input("Ingrese la palabra clave para decifrar: \n\t")
                        mfra1=VSINTD(clave)
                        mfra2=depurar(mfra1)
                        mfra4=Minus(mfra2)
                        decodificacion=decodificacionMono(mfra3, mfra4)
                        print("Texto original: ",mfra3)
                        print("Texto decodificado: ",decodificacion)
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