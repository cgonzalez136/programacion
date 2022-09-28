from asyncio.windows_events import NULL
import datetime
fecha = datetime.datetime.now()
option2 = 1
LLAVE = 0
NOMBRE = "NO REGISTRADO"
EDAD = "NO REGISTRADO"
RUT = "NO REGISTRADO"
PATENTE_DEL_VEHICULO = "NO REGISTRADO"
while (option2 == 1) or (LLAVE == 1):
    print ("Bienvenido a UBER que desea hacer hoy?")
    option1= int(input("PRESIONE \n '1' PARA REGISTRARSE (OBLIGATORIO) \n '2' PARA COMENZAR UNA CARRERA \n '3' PARA CONSULTAR DATOS \n '4' SALIR DE LA APLICACION UBER \n"))
    if (option1 == 1):
        option2 = 2
        while (option2 == 2 ):
            NOMBRE = input("Ingrese su nombre ")
            EDAD = input("Ingrese su edad ")
            RUT =int(input("Ingrese su rut (SIN PUNTOS, NI GUION) "))
            PATENTE_DEL_VEHICULO =input("Ingrese patente del vehiculo ")
            option2=int(input("Esta seguro que quiere continuar? '1' = Si  '2' = No \n"))
            LLAVE=1
    if (option1 == 2):
        if (LLAVE==0):
            print("\n DEBE REGISTRARSE ANTES DE PODER HACER UNA CARRERA \n volviendo a menu.....")
        if (LLAVE== 1):
            print ("\n Usted esta empezando una carrera \n")
            X = int(input("Inserte la destinacion (LATITUD) (Y) en METROS "))
            Y = int(input("Inserte la destinacion (LONGITUD) (X) en METROS "))
            X1= 0
            Y2= 0
            print("\n Bienvenido al sistema de navegacion de UBER, primero, Al acelerar aumentara la velocidad a 10km/h (2,7m/s) \n Por cada metro se cobraran 50 pesos \n")
            while (X1 != X and Y2 != Y):
                boton1= 0
                velocidad = 0
                apagado= 0
                encender=int(input("1- Encender Automovil \n"))
                if (encender == 1):
                    while (apagado != 3):
                        X1 = -9999 if X1 < -9999 else X if X1 > X else X1
                        print("\nRECORDATORIO SU DESTINACION ESTA EN ",X," (X), ",Y," (Y) \nSu distancia recorrida es de  ",X1," (X)")
                        print("Su velocidad actual es de ",velocidad,"m/s \n")
                        print("1- Acelerar Automovil")
                        print("2- Girar Automovil")
                        print("3- Apagar automovil y detener ")
                        print("4- Avanzar (", velocidad * 10, " metros)")
                        boton1=int(input("Seleccione "))
                        if (X1 == X):
                            print("\n Hay una pared a continuacion, Porfavor gire o termine su recorrido si ya ha llegado apagando el vehiculo. \n")
                        if (boton1 == 3):
                            apagado = 3
                        if (boton1 == 1):
                            velocidad = 2.7 + velocidad
                        if (boton1==4):
                            X1 = X1 + (velocidad * 10)
                        if (boton1 == 2):
                            boton1 = 0
                            while (boton1 != 2) and (apagado != 3):                    
                                Y2 = -9999 if Y2 < -9999 else Y if Y2 > Y else Y2
                                print("\n RECORDATORIO SU DESTINACION ESTA EN ",X," (X), ",Y," (Y)")
                                print("Su distancia recorrida es de ",Y2,"(Y)")
                                print("Su velocidad actual es de ",velocidad,"m/s")
                                print("1- Acelerar Automovil")
                                print("2- Girar Automovil")
                                print("3- Apagar automovil y detener")
                                print("4- Avanzar ", velocidad * 10," metros \n")
                                if (Y2==Y):
                                    print("\n Hay una pared a continuacion, Porfavor gire o termine su recorrido si ya ha llegado apagando el vehiculo.")
                                boton1=int(input("Seleccione "))
                                if (boton1==3):
                                    apagado = 3
                                    boton1 = 2
                                if (boton1 == 1):
                                    velocidad = 2.7 + velocidad
                                if (boton1 == 4):
                                    Y2 = Y2 + (velocidad * 10)
            print("\nUSTED RECORRIO = ", (X+Y), " METROS")
            print("PRECIO QUE DEBE PAGAR EL CLIENTE= ", (X+Y)*50, "$")
            print("USTED ENTREGO AL CLIENTE a las", fecha,)
            respuesta=int(input("\n Llegaste a tu destino 1- Volver al menu "))
    if (option1 == 3):
        print("\n NOMBRE DE EMPLEADO:", NOMBRE, "\n EDAD:", EDAD, "\n RUT:", RUT, "\n PATENTE DEL AUTOMOVIL:", PATENTE_DEL_VEHICULO)
        ok=input("Presione cualquier tecla para volver al menu ")
    if (option1 == 4):
        option2 = 10
        LLAVE == 0                            
                            
                        
                        
            
            

    
    

