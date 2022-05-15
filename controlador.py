#!/usr/bin/python3
"""Este archivo contiene el codigo para aceptar las entradas del usuario y delega la 
representación de datos a una Vista y el manejo de datos a un Modelo."""
import operaciones_CRUD
from modelo import Modelo
from vista import Vista


class Controlador():
    """esta clase contiene los metodos para aceptar las entradas del usuario"""
    def __init__(self):
        self.modelo = Modelo()
        self.vista = Vista()
    
    def mostrar_bienvenida(self):
        self.vista.mostrar_bienvenida()

    def registrar(self):
        #pregunta documento para saber si existe o crear uno
        self.vista.registrar()
        documento = int(input('Numero de documento: '))
        info = self.modelo.mostrar_jugador(documento)
        self.vista.mostrar_jugador(info)

        if (info.shape[0] == 0):

            self.vista.solicitar_datos_jugador()
            nombre = input('nombre: ')
            apellido = input('apellido: ')
            self.modelo.crear_jugador(documento, nombre, apellido)
            info_2 = self.modelo.mostrar_jugador(documento)
            self.vista.mostrar_jugador(info_2)

        return documento


    def mostrar_informacion_ronda(self, nivel):
        self.vista.mostrar_informacion_ronda(nivel)
        info = self.modelo.mostrar_todo_pregunta(nivel)
        self.vista.mostrar_preguntas_con_respuestas(info)

        # extraer en que posicion esta la respuesta correcta
        serie_respuestas = info['veracidad']
        id_pregunta = info.iloc[0, 3]
        respuestas_id = list(info['id_opciones'])
        for index, value in serie_respuestas.items():
            if (value == 1):
                posicion_respuesta = index
        return posicion_respuesta, id_pregunta, respuestas_id

    def seguir_si_no(self):
        self.vista.seguir_si_no()
        decision = input('seguir? ')
        return (decision == '1') 
    
    def responder_pregunta(self, respuesta_secreta, respuestas_id):
        self.vista.preguntar_respuesta()
        eleccion = input('ingrese la letra: ')
        diccionario_respuestas = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
        try:
            mapeo = diccionario_respuestas[eleccion]
            acierto = (mapeo == respuesta_secreta)
            id_respuesta = respuestas_id[mapeo]

            return acierto, id_respuesta
        except:
            acierto = False
            id_respuesta = None
            return acierto, id_respuesta

    def guardar_registro_historico(self, fecha, retiro, idjugador, idpregunta, idopciones, idronda):
        self.modelo.guardar_registro_historico(fecha, retiro, idjugador, idpregunta, idopciones, idronda)

    def mostrar_acumulado(self, fecha, id_jugador):
        info = self.modelo.mostrar_acumulado_fecha(fecha, id_jugador)
        self.vista.mostrar_acumulado_fecha(info)

    def despedir_jugador(self):
        self.vista.despedir_jugador()

    def felicitar_jugador(self):
        self.vista.felicitar_jugador()
