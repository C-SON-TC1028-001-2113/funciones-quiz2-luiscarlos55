# Escribe tus funciones abajo de esta línea
# 1ft = 30.48 cm
    # 1'' = 2.54 cm
    # 1yrds = 91.44 cm
def main():
    # Escribe tu código abajo de esta línea
    opciones=int(input("1. pies a centimetros, 2. pulgadas a centimetros, 3. yardas a centimentros " 
                "Introduce una opcion: "))
    if opciones==1:
        pies=int(input('Introduce la cantidad: '))
        cm= pies*30.48 
        print('Los pies equivalen en cm a ' +str(cm))
    elif opciones==2:
        pulgadas=int(input('Introduce la cantidad: '))
        cm2= pulgadas*2.54 
        print('Las pulgadas equivalen en cm a ' +str(cm2))
    elif opciones==3:
        yardas=int(input('Introduce la cantidad: '))
        cm3= yardas*91.44 
        print('Las yardas equivalen en cm a ' +str(cm3))

if __name__ == '__main__':
    main()
