#!/usr/bin/python3
"""Este archivo contiene el codigo para gestionar los datos y define reglas y comportamientos."""
import operaciones_CRUD

class Modelo():
    """metodos para gestionar los datos"""
    def __init__(self):
        self.conexion = operaciones_CRUD.crear_conexion()


    
    def crear_jugador(self,id_jugador, nombre, apellido):
        operaciones_CRUD.crear_jugador(self.conexion, id_jugador, nombre, apellido)

    def crear_jugadores(self, lista_jugadores):
        operaciones_CRUD.crear_multiples_jugadores(self.conexion, lista_jugadores)

    def mostrar_jugador(self, id_jugador):
        return  operaciones_CRUD.mostrar_jugador(self.conexion, id_jugador)

    def mostrar_todo_pregunta(self, nivel):
        return operaciones_CRUD.mostrar_preguntas_opciones_r(self.conexion, nivel)

    def guardar_registro_historico(self, fecha, retiro, idjugador, idpregunta, idopciones, idronda):
        operaciones_CRUD.crear_registro_historico(self.conexion, fecha, retiro, idjugador, idpregunta, idopciones, idronda)

    def mostrar_acumulado_fecha(self, fecha, id_jugador):
        return operaciones_CRUD.mostrar_acumulado_fecha(self.conexion, fecha, id_jugador)
