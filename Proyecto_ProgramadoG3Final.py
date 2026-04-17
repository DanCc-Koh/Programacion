#DEPURAR LA FRASE
"""
Cambiar los espacios de inicio y final
Cambiar el try except en Cesar
Expandir Diccionario manual de depurar vocales
"""




#Descripcion: Recibe la frase o palabra que ingrese el usuario y remueve todo tipo de tilde, dierecis, etc... que se encuentren en las vocales
#Entrada: Recibe la palabra o frase tenga o no tildes o dierecis
#Salida: Devuelve la frase o palabra sin las tildes o dierecis que tenia la original
#restricciones: N/A
def Depurar_Vocales (Palabra):
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
def Depurar_Simbolos(Palabra):
    Alfa_Min =("abcdefghijklmnñopqrstuvwxyz")
    Alfa_Mayus=("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
    Corregido=[]
    for letra in Palabra:
        if letra in Alfa_Min or letra in Alfa_Mayus:
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
    Minuscula=F.lower()
    return Minuscula

#DEPURAR LA FRASE
""" Cod Cesar"""

#Descripción:
#Entradas:
#Salidas:
#Restricciones:
def Vacio(Frase_Final):
    Reinicio=False
    while Reinicio==False:
        print("\n¡¡¡ADVERTENCIA!!!\n\n La frase transformada no posee ninguna letra\n por lo que el programa no podra devolver un valor\n\n Si desea reiniciar el programa, ingrese 1\n\n Si desea cancelar programa Ingrese 2\n\n")
        OP=input()
        if OP== "1":
            Frase = input("Ingrese la frase anterior corregida o una nueva: \n\t")
            Frase1 = Depurar_Vocales(Frase)
            Frase2 = Depurar_Simbolos(Frase1)
            Frase_Final = Minus(Frase2)
            print("Frase transformada:", Frase_Final)
            if Frase=="":
                while Frase =="":
                    Frase = input("El valor de la frase no puede ser vacío: \n\t")
                    print("Frase ingresada:", Frase)
                    Frase1 = Depurar_Vocales(Frase)
                    Frase2 = Depurar_Simbolos(Frase1)
                    Frase_Final = Minus(Frase2)
                    print("Frase transformada:", Frase_Final)
                if Frase_Final == "":
                    while Frase_Final=="":
                        print("Frase ingresada:", Frase)
                        print("Frase transformada:", Frase_Final)
                        print("\nLa frase transformada sigue vacía. Intente otra vez.")
                        Frase = input()
                        Frase1 = Depurar_Vocales(Frase)
                        Frase2 = Depurar_Simbolos(Frase1)
                        Frase_Final = Minus(Frase2)
                        print("Frase transformada:", Frase_Final)
                    return Frase_Final
                else:
                    return Frase_Final
            if Frase_Final=="":
                while Frase_Final=="":
                            print("Frase ingresada:", Frase)
                            print("Frase transformada:", Frase_Final)
                            print("\nLa frase transformada sigue vacía. Intente otra vez.")
                            Frase = input()
                            Frase1 = Depurar_Vocales(Frase)
                            Frase2 = Depurar_Simbolos(Frase1)
                            Frase_Final = Minus(Frase2)
                            print("Frase transformada:", Frase_Final)
                return Frase_Final
            else:
                    return Frase_Final
        elif OP=="2":
            Menu=False
            Reinicio=True
            return Menu
        else:
            print("ingrese un valor valido")
    Frase1 = Depurar_Vocales(Frase)
    Frase2 = Depurar_Simbolos(Frase1)
    Frase_Final = Minus(Frase2)
    print("Frase transformada:", Frase_Final)
    return Frase_Final

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
        Letra_Actual = frase[i]
        if Letra_Actual == " ":
            frase_codificada = frase_codificada + " "
        else:
            letra_min = Letra_Actual.lower()
            if letra_min in alfabeto:
                pos_a = -1
                contador = 0
                while contador < len(alfabeto):
                    if alfabeto[contador] == letra_min:
                        pos_a = contador
                    contador = contador + 1
                Nueva_Posicion = pos_a + desplazamiento
                while Nueva_Posicion > 26:
                    Nueva_Posicion = Nueva_Posicion - 27
                while Nueva_Posicion < 0:
                    Nueva_Posicion = Nueva_Posicion + 27
                let_fin = alfabeto[Nueva_Posicion]
                frase_codificada = frase_codificada + let_fin
    return frase_codificada

#Descripción: Decodifica una frase textual utilizando el método de César al inverso.
#Entrada: frase textual codificada, número desplazamiento
#Salida: Texto original
#Restricciones: desplazamiento entero

def DecoCesar(frase, desplazamiento):
    if frase == " ":
        return " "
    desplazamiento_inv = desplazamiento * -1
    Resultado_2 = CodCesar(frase, desplazamiento_inv)
    return Resultado_2
""" Cod Cesar"""



""" Cod Monoalfabetico """
#Descripción:
#Entradas:
#Salidas:
#Restricciones:
def depurarClave(claveOriginal):
    if claveOriginal=="": 
        NoVacio=True  
        while NoVacio==True:
            claveOriginal=str(input("La clave no puede ser un valor vacio: \n\t"))
            Clave1=Depurar_Vocales(claveOriginal)
            Clave2=Depurar_Simbolos(Clave1)
            Clave3=Minus(Clave2)
            if Clave3!="":
                NoVacio=False
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
def CodMono(texto, claveOriginal):
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
def DecodMono(textoCifrado, clave): 
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
        ValorVacio=""
        while ValorVacio=="":
                clave=str(input("La clave no puede ser un valor vacio: \n\t"))
                DepurarClave=Depurar_Vocales(clave)
                DepurarSimbolos=Depurar_Simbolos(DepurarClave)
                Minusculas=Minus(DepurarSimbolos)

    Alfabeto =("abcdefghijklmnñopqrstuvwxyz")
    EspacioF=[]
    Espacios_frase=frase.find(" ")
    EspacioC=[]
    Espacios_Clave=clave.find(" ")
    Num1=[]
    for letra in frase:
        if letra in Alfabeto:
            X=Alfabeto.find(letra)
            Num1.append(X)
    while Espacios_frase!=-1:
        EspacioF.append(Espacios_frase)
        Espacios_frase=frase.find(" ",Espacios_frase+1)

    Num2=[]
    while len(Num1)>len(Num2): 
        for letra in clave:
            if letra in Alfabeto:
                X=Alfabeto.find(letra)
                Num2.append(X)
            else:
                if letra==" ":  
                    EspacioC.append(clave.index(letra))
    while Espacios_Clave!=-1:
        EspacioC.append(Espacios_Clave)
        Espacios_Clave=clave.find(" ",Espacios_Clave+1)


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
def DecodiVigenere(frase,clave):
    if clave == "":
        while clave=="":
            clave=str(input("La clave no puede ser un valor vacio: \n\t"))
    Alfabeto =("abcdefghijklmnñopqrstuvwxyz")
    Num1=[]
    Espacio_Encrip=[]
    Encriptado=frase.find(" ")
    Espacio_Clave=[]
    Espacio_clave=clave.find(" ")

    Num1=[]
    for letra in Frase_Final:
        if letra in Alfabeto:
            X=Alfabeto.find(letra)
            Num1.append(X)
    while Encriptado!=-1:
        Espacio_Encrip.append(Encriptado)
        Encriptado=frase.find(" ",Encriptado+1)

    Num2=[]
    while len(Num1)>len(Num2): 
        for letra in clave:
            if letra in Alfabeto:
                X=Alfabeto.find(letra)
                Num2.append(X)
            else:
                if letra==" ":  
                    Espacio_Clave.append(Espacio_clave.index(letra))
    while Espacio_clave!=-1:
        Espacio_Clave.append(Espacio_clave)
        Espacio_clave=clave.find(" ",Espacio_clave+1)

    Num3=[]
    for a, b in zip(Num1, Num2):
        Resultado=a-b
        if Resultado<0:
            Resultado=27-abs(Resultado)
            Num3.append((Resultado))
        else:
            Num3.append((Resultado))

    Decodificar=[]
    for num in Num3:
        letra=Alfabeto[num]
        Decodificar.append(letra)
    if Espacio_Encrip!=[]:
        for i in range(len(Espacio_Encrip)):
            Espacio=Espacio_Encrip[i] 
            Decodificar.insert( Espacio," ")
    Respuesta="".join(Decodificar)
    return Respuesta

#
#
#
#
def Dostecnicas(opcion1,opcion2):
    global Frase_Final
    Cesar="1"
    Monosi="2"
    Vigenere="3"
    Reinicio1=True
    while Reinicio1==True:
        if opcion1==Cesar:
                desplazamiento = int(input("Ingrese la cantidad de posiciones a desplazar (ejemplo 3): "))
                Encrip_Cesar = CodCesar(Frase_Final, desplazamiento)
                print()
                Frase_Final=Encrip_Cesar
                Reinicio1=False
                
        elif opcion1==Monosi:
            clave=input("Ingrese la palabra clave para codificar (Para Monoalfabetico): \n\t")
            Frase1=Depurar_Vocales(clave)
            Frase2=Depurar_Simbolos(Frase1)
            Frase3=Minus(Frase2)
            cifrado=CodMono(Frase_Final, Frase3)
            Frase_Final=cifrado
            print()

            Reinicio1=False

        elif opcion1==Vigenere:
            Clave=input("Ingrese la palabra clave para codificar (Para Vigenere): \n\t")
            Clave1=Depurar_Vocales(Clave)
            Clave2=Depurar_Simbolos(Clave1)
            Clave_Final=Minus(Clave2)
            Encriptado=CodiVigenere(Frase_Final,Clave_Final)
            if Encriptado=="":
                print("\n No fue posible realizar la encriptacion debido que la frase ingresada\n NO poseia ningun tipo de letra")
            else:
                Frase_Final=Encriptado
                Reinicio1=False
                print()
        else:
            print("Opcion no valida,\n\t1.César\n\t2.Monoalfabético\n\t3.Vigénere")
            opcion1=input()

    Reinicio2=True
    while Reinicio2==True:
        if opcion2==Cesar:
                desplazamiento = int(input("Ingrese la cantidad de posiciones a desplazar (ejemplo 3): "))
                Encrip_Cesar = CodCesar(Frase_Final, desplazamiento)
                print("Palabra encriptada (César): ", Encrip_Cesar)
                print()
                Reinicio2=False

        elif opcion2==Monosi:
            clave=input("Ingrese la palabra clave para codificar (Para Monoalfabetico): \n\t")
            Frase1=Depurar_Vocales(clave)
            Frase2=Depurar_Simbolos(Frase1)
            Frase3=Minus(Frase2)
            cifrado=CodMono(Frase_Final, Frase3)
            print("Texto encriptada: ",cifrado)
            print()
            Reinicio2=False
        elif opcion2==Vigenere:
            Clave=input("Ingrese la palabra clave para codificar (Para Vigenere): \n\t")
            Clave1=Depurar_Vocales(Clave)
            Clave2=Depurar_Simbolos(Clave1)
            Clave_Final=Minus(Clave2)
            Encriptado=CodiVigenere(Frase_Final,Clave_Final)
            if Encriptado=="":
                print("\n No fue posible realizar la encriptacion debido que la frase ingresada\n NO poseia ningun tipo de letra")
            else:
                print("Palabra encriptada: ",Encriptado)
            Reinicio2=False
            print()
        else:
            print("Opcion no valida,\n\t1.César\n\t2.Monoalfabético\n\t3.Vigénere")
            opcion2=input()
    return

#
#
#
#
def TresTecnicas(opcion1,opcion2,opcion3):
    global Frase_Final
    Cesar="1"
    Monosi="2"
    Vigenere="3"
    Reinicio1=True
    while Reinicio1==True:
        if opcion1==Cesar:
            desplazamiento = int(input("Ingrese la cantidad de posiciones a desplazar (ejemplo 3): "))
            Encrip_Cesar = CodCesar(Frase_Final, desplazamiento)
            print()
            Frase_Final=Encrip_Cesar
            Reinicio1=False

        elif opcion1==Monosi:
            clave=input("Ingrese la palabra clave para codificar (Para Monoalfabetico): \n\t")
            clave1=Depurar_Vocales(clave)
            clave2=Depurar_Simbolos(clave1)
            clave3=Minus(clave2)
            cifrado=CodMono(Frase_Final, clave3)
            Frase_Final=cifrado
            print()
            Reinicio1=False

        elif opcion1==Vigenere:
            Clave=input("Ingrese la palabra clave para codificar (Para Vigenere): \n\t")
            clave1=Depurar_Vocales(Clave)
            clave2=Depurar_Simbolos(clave1)
            clave3=Minus(clave2)
            Encriptado=CodiVigenere(Frase_Final,clave3)
            if Encriptado=="":
                print("\n No fue posible realizar la encriptacion debido que la frase ingresada\n NO poseia ningun tipo de letra")
            else:
                Frase_Final=Encriptado
                Reinicio1=False
                print()
        else:
            print("Opcion no valida,\n\t1.César\n\t2.Monoalfabético\n\t3.Vigénere")
            opcion1=input()


    Reinicio2=True
    while Reinicio2==True:
        if opcion2==Cesar:
            desplazamiento = int(input("Ingrese la cantidad de posiciones a desplazar (ejemplo 3): "))
            Encrip_Cesar = CodCesar(Frase_Final, desplazamiento)
            print()
            Frase_Final=Encrip_Cesar
            Reinicio2=False

        elif opcion2==Monosi:
            clave=input("Ingrese la palabra clave para codificar (Para Monoalfabetico): \n\t")
            clave1=Depurar_Vocales(clave)
            clave2=Depurar_Simbolos(clave1)
            clave3=Minus(clave2)
            cifrado=CodMono(Frase_Final, clave3)
            Frase_Final=cifrado
            print()

            Reinicio2=False

        elif opcion2==Vigenere:
            Clave=input("Ingrese la palabra clave para codificar (Para Vigenere): \n\t")
            clave1=Depurar_Vocales(Clave)
            clave2=Depurar_Simbolos(clave1)
            clave3=Minus(clave2)
            Encriptado=CodiVigenere(Frase_Final,clave3)
            if Encriptado=="":
                print("\n No fue posible realizar la encriptacion debido que la frase ingresada\n NO poseia ningun tipo de letra")
            else:
                Frase_Final=Encriptado
                Reinicio2=False
                print()
        else:
            print("Opcion no valida,\n\t1.César\n\t2.Monoalfabético\n\t3.Vigénere")
            opcion1=input()


    Reincio3=True
    while Reincio3==True:
        if opcion3==Cesar:
            try:
                desplazamiento = int(input("Ingrese la cantidad de posiciones a desplazar (ejemplo 3): "))
                Encrip_Cesar = CodCesar(Frase_Final, desplazamiento)
                print("Palabra encriptada (César): ", Encrip_Cesar)
                print()
            except ValueError:
                print("ERROR: Debe ingresar un número entero para el desplazamiento")
                print()
                desplazamiento = int(input("Ingrese la cantidad de posiciones a desplazar (ejemplo 3): "))
            Reincio3=False

        elif opcion3==Monosi:
            clave=input("Ingrese la palabra clave para codificar (Para Monoalfabetico): \n\t")
            clave1=Depurar_Vocales(clave)
            clave2=Depurar_Simbolos(clave1)
            clave3=Minus(clave2)
            cifrado=CodMono(Frase_Final, clave3)
            print("Texto encriptada: ",cifrado)
            print()
            Reincio3=False
        elif opcion3==Vigenere:
            Clave=input("Ingrese la palabra clave para codificar (Para Vigenere): \n\t")
            clave1=Depurar_Vocales(Clave)
            clave2=Depurar_Simbolos(clave1)
            clave3=Minus(clave2)
            Encriptado=CodiVigenere(Frase_Final,clave3)
            if Encriptado=="":
                print("\n No fue posible realizar la encriptacion debido que la frase ingresada\n NO poseia ningun tipo de letra")
            else:
                print("Palabra encriptada: ",Encriptado)
            Reincio3=False
            print()
        else:
            print("Opcion no valida,\n\t1.César\n\t2.Monoalfabético\n\t3.Vigénere")
            opcion2=input()
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
    Frase1=Depurar_Vocales(Frase)
    Frase2=Depurar_Simbolos(Frase1)
    Frase_Final=Minus(Frase2)
    print("Frase transformada: ",Frase_Final)
    while Frase_Final=="":
        Frase_Final=Vacio(Frase_Final)
        if Frase_Final==False:
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
                    while Frase_Final=="":
                        Frase=str(input("El valor de la frase no puede ser vacio: \n\t"))
                        Frase1=Depurar_Vocales(Frase)
                        Frase2=Depurar_Simbolos(Frase1)
                        Frase_Final=Minus(Frase2)
                else:
                    print("Frase ingresada: ",Frase)
                    Frase1=Depurar_Vocales(Frase)
                    Frase2=Depurar_Simbolos(Frase1)
                    Frase_Final=Minus(Frase2)
                    print("Frase transformada: ",Frase_Final)
                    while Frase_Final=="":
                        Frase_Final=Vacio(Frase_Final)
                        if Frase_Final==False:
                            Menu=False
                    Menu0=False
                Frase1=Depurar_Vocales(Frase)
                Frase2=Depurar_Simbolos(Frase1)
                Frase_Final=Minus(Frase2)
                Menu0=False
        else:
            Menu1=True
            Menu2=True
            Opcion=(input("¿Que desea hacer con la frase?\n\t 1.Codificar\n\t 2.Decodificar \n\t 3.Cancelar \n\t"))
            if Opcion=="1":
                """ MENU PARA CODIFICAR """

                while Menu1==True:
                    Menu2=True
                    Opcion2=(input("Ingrese la cantidad de tecnicas que desea realizar (de 1 a 3) o 4 para Cancelar \n\t"))
                    if Opcion2=="1":
                        while Menu2==True:
                            Opcion1=(input("Cual desea utilizar: \n\t1.César\n\t2.Monoalfabético\n\t3.Vigénere\n\t4.Cancelar \n\t"))
                            if Opcion1=="1":
                                    print("César")
                                    desplazamiento = int(input("Ingrese la cantidad de posiciones a desplazar (ejemplo 3): "))
                                    Encrip_Cesar = CodCesar(Frase_Final, desplazamiento)
                                    print("\n Palabra original: ", Frase_Final)
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


                            elif Opcion1=="2":
                                print("Monoalfabético")
                                clave=input("Ingrese la palabra clave para codificar: \n\t")
                                Frase1=Depurar_Vocales(clave)
                                Frase2=Depurar_Simbolos(Frase1)
                                Frase_Final2=Minus(Frase2)
                                cifrado=CodMono(Frase_Final, Frase_Final2)
                                print("Texto original: ",Frase_Final)
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

                            
                            elif Opcion1=="3":
                                print("Vigénere")
                                Clave=input("Ingrese la palabra clave para codificar: \n\t")
                                Clave1=Depurar_Vocales(Clave)
                                Clave2=Depurar_Simbolos(Clave1)
                                Clave3=Minus(Clave2)
                                Encriptado=CodiVigenere(Frase_Final,Clave3)
                                if Encriptado=="":
                                    print("\n No fue posible realizar la encriptacion debido que la frase ingresada\n NO poseia ningun tipo de letra")
                                else:
                                    print("Palabra original: ",Frase_Final)
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

                            elif Opcion1=="4":
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

                    elif Opcion2=="2":
                        while Menu2==True:
                            Opcion1=(input("Cuales 2 tecnicas desea utilizar (Indique la primera y segunda por separado): \n\t1.César\n\t2.Monoalfabético\n\t3.Vigénere\n\t4.Cancelar\n\t"))
                            Opcion2=(input("\n\t"))
                            if Opcion1=="4" or Opcion2=="4":
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
                            elif Opcion1=="1" or Opcion2=="1" or Opcion1=="2" or Opcion2=="2" or Opcion1=="3" or Opcion2=="3":
                                Dostecnicas(Opcion1,Opcion2)
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

                    elif Opcion2=="3":
                        while Menu2==True:
                            Opcion1=(input("Ingrese el orden que desea utilizar, 1 a la vez: \n\t1.César\n\t2.Monoalfabético\n\t3.Vigénere\n\t4.Cancelar\n\t"))
                            Opcion2=(input("\n\t"))
                            Opcion3=(input("\n\t"))
                            if Opcion1=="4" or Opcion2=="4" or Opcion3=="4":
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
                            elif Opcion1=="1" or Opcion2=="1" or Opcion3=="1" or Opcion1=="2" or Opcion2=="2" or Opcion3=="2" or Opcion1=="3" or Opcion2=="3" or Opcion3=="3":
                                TresTecnicas(Opcion1,Opcion2,Opcion3)
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


                    elif Opcion2=="4":
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

            elif Opcion=="2":
                """ MENU PARA DECODIFICAR """

                print("Decodificar")
                while Menu2==True:
                    Opcion1=(input("Cual desea utilizar: \n\t1.César\n\t2.Monoalfabético\n\t3.Vigénere\n\t4.Cancelar \n\t"))
                    if Opcion1=="1":
                        print("César")
                        desplazamiento = int(input("Ingrese el número de desplazamiento original: "))
                        DecoCesar = DecoCesar(Frase_Final, desplazamiento)
                        print("\n Palabra original encriptada: ", Frase_Final)
                        print("Palabra desencriptada: ", DecoCesar)
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



    #DECODIFICACIÓN MONOALFABÉTICO

                    
                    elif Opcion1=="2":
                        print("Monoalfabético")
                        clave=input("Ingrese la palabra clave para decifrar: \n\t")
                        Frase1=Depurar_Vocales(clave)
                        Frase2=Depurar_Simbolos(Frase1)
                        Frase_Final2=Minus(Frase2)
                        decodificacion=DecodMono(Frase_Final, Frase_Final2)
                        print("Texto original: ",Frase_Final)
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
                    elif Opcion1=="3":
                        print("Vigénere")
                        Clave=input("Ingrese la palabra clave para Decodificar: \n\t")
                        Clave1=Depurar_Vocales(Clave)
                        Clave2=Depurar_Simbolos(Clave1)
                        Clave3=Minus(Clave2)
                        Decodificar=DecodiVigenere(Frase_Final,Clave3)
                        if Decodificar=="":
                            print( "\n No fue posible realizar la desencriptacion debido a que la frase ingresada\n NO poseia ningun tipo de letra")
                        else:
                            print("Palabra original encriptada: ",Frase_Final)
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

                    elif Opcion1=="4":
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
            elif Opcion=="3":
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