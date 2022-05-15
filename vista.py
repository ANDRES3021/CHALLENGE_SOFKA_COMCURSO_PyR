#!/usr/bin/python3
"""Este archivo contiene el codigo para presentar los datos al usuario."""
class Vista():
    """metodos para mostrar datos usuario"""
    
    def adornar(func):
        SEPARADOR = '*'

        def funcion_interna(*args, **kwargs):
            print(SEPARADOR * 30)
            func(*args, **kwargs)
            print(SEPARADOR * 30)

        return funcion_interna


    @adornar
    def mostrar_jugador(self, info):
        """info es el resultado de la consulta"""
        
        print('Se encontro la siguiente informacion de jugador: ')
        print(info)

    @adornar
    def mostrar_bienvenida(self):
        print('Bienvenido(a) a el juego')

    @adornar
    def registrar(self):
        print('Debemos verificar si esta o no registrado, por favor ingrese su numero de documento y presione enter')

    @adornar
    def solicitar_datos_jugador(self):
        print('Por favor ingrese su nombre y apellido para crear su usuario')

    @adornar
    def mostrar_informacion_ronda(self, nivel):
        print(f"usted va en el nivel: {nivel}")
    
    @adornar
    def mostrar_preguntas_con_respuestas(self, info):
        print(info.iloc[0, 0])
        print('(A)',info.iloc[0, 1])
        print('(B)',info.iloc[1, 1])
        print('(C)',info.iloc[2, 1])
        print('(D)',info.iloc[3, 1])

    @adornar
    def seguir_si_no(self):
        print('si desea seguir jugando presione 1, de lo contrario presione cualquier tecla')

    @adornar
    def preguntar_respuesta(self):
        print('seleccione la letra de la respuesta que usted cree es la correcta')
        print('NOTA!! si ingresa una opcion que no esta, se considera como respuesta erronea')

    @adornar
    def mostrar_acumulado_fecha(self, info):
        print(f"su acumulado es de: {info.iloc[0,0]} $")


    @adornar
    def despedir_jugador(self):
        print('lo sentimos, muchas gracias por participar')

    @adornar
    def felicitar_jugador(self):
        print('Felicidades, ha ganado el juego')
