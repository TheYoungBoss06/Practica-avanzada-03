resultado = 0
def calcular_suma(resultado):

    while True:
        try:
            suma1 = int(input('Introduce el primer numero : '))
            suma2 = int(input('Introduce el segundo numero: '))
            resultado = suma1 + suma2
            if suma1 and suma2:
                print(f'El resultado de la suma es: {resultado}:\n ')
            else:
                break
            
        except ValueError:
            print('Por favor, Introduce numero valido: \n')
            return resultado
        
def calcular_resta(resultado):

    while True:
        try:
            resta1 = int(input('Introduce el primer numero: '))
            resta2 = int(input('Introduce el segundo numero:'))
            resultado = resta1 - resta2
            if resta1 and resta2:
                print(f'El resultado de la Resta es: {resultado}:\n ')
            else:
                break
            
        except ValueError:
            print('Por favor, Introduce numero valido: \n')
            return resultado
        
def calcular_dividir(resultado):

    while True:
        try:
            resta1 = int(input('Introduce el primer numero: '))
            resta2 = int(input('Introduce el segundo numero: '))
            resultado = resta1 / resta2
            if resta1 and resta2:
                print(f'El resultado de la Divicion es: {resultado}:\n ')
            else:
                break
            
        except ValueError:
            print('Por favor, Introduce numero valido: \n')
            return resultado
        

def calcular_multiplicar(resultado):

    while True:
        try:
            resta1 = int(input('Introduce el primer numero: '))
            resta2 = int(input('Introduce el segundo numero: '))
            resultado = resta1 * resta2
            if resta1 and resta2:
                print(f'El resultado de la Multiplicacion es: {resultado}:\n ')
            else:
                break
            
        except ValueError:
            print('Por favor, Introduce numero valido: \n')
            return resultado
        
        

def calcular_porciento(resultado):

    while True:
        try:
            porsiento1 = int(input('Introduce el primer numero: '))
            porsiento2 = int(input('Introduce el porcentaje:: '))
            resultado = (porsiento2 / 100)* porsiento1 
            if porsiento1 and porsiento2:
                print(f'El porciento del un numero es: {resultado}:\n ')
            else:
                break
            
        except ValueError:
            print('Por favor, Introduce numero valido: \n')
            return resultado
        

def calcular_resto(resultado):

    while True:
        try:
            resto1 = int(input('Introduce el primer numero: '))
            resto2 = int(input('Introduce el segundo numero: '))
            resultado = resto1 % resto2
            if resto1 and resto2:
                print(f'El resto de la division es: {resultado}:\n ')
            else:
                break
            
        except ValueError:
            print('Por favor, Introduce numero valido: \n')
            return resultado
        

def menu():
    print('\n  ---------------------------------- MENU ---------------------------------------\n')
    print(' <                       1: Seleccione para sumar:                                > ')
    print(' <                       2: Seleccione para restar:                               > ')
    print(' <                       3: Seleccione para dividir:                              > ')
    print(' <                       4: Seleccione para Multiplicar:                          > ')
    print(' <                       5: Seleccione para Encontrar  porciento:                 > ')
    print(' <                       6: Seleccione para Encontrar el resto de una división:   > ')
    print(' <                       7: Seleccione para Calcular el numero entero:            > ')
    print(' <                       8: Seleccione para Encontrar el numero primo:            > ')
    print(' <                          Escribe Salir, Para cerrar el programa:               > ')
    print('__________________________________________________________________________________\n')
    
    