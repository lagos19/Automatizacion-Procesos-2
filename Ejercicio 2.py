print('***** Registro de Pais ******')
print('*      1 Honduras           *')
print('*      2 Costa Rica         *')
print('*      3 Guatemala          *') 
print('*      4 Mexico             *')
print('*      5 Salvador           *')
print('****************************************')
Pais = {'Honduras':9.746, 'Costa Rica':5.048 , 'Guatemala':16.6, 'Mexico':128.96,'Salvador':6.454}
Poblacion = input('Ingrese el nombre del pais : ').title()

if Poblacion in Pais:
    print( 'La Poblacion de', Poblacion, 'es', Pais[Poblacion], 'Millones de habitantes')
else: 
    print("Lo siento, el Pais", Poblacion, "No está disponible, Favor Ingresar Pais regitrado.")