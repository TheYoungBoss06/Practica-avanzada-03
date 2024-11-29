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