#!/usr/bin/python3
"""archivo que contiene las operaciones CRUD implemantadas"""
import sqlite3
from sqlite3 import IntegrityError
from functools import wraps
from tkinter import Variable
import pandas as pd

def crear_conexion():
    conexion=sqlite3.connect("base_datos.db")
    return conexion

def conectar(func):
    """ decorador para evitar repetir codigo"""
    @wraps(func) # evita que sobreescriba el nombre de la funcion.
    def funcion_interna(conexion, *args, **kwargs):

        if ('mostrar' in func.__name__):
            query = func(*args, **kwargs)
            df = pd.read_sql_query(query, conexion)
            return df
        else:
            if ('multiples' in func.__name__):
                query, lista = func(*args, **kwargs)
                try:
                    instruccion = conexion.executemany(query, lista)
                except IntegrityError:
                    print('alguno de los registros ya existe, por favor verifique')
            else:
                query = func(*args, **kwargs)
                try:
                    instruccion = conexion.execute(query)
                except IntegrityError:
                    print('el registro ya existe, por favor ingrese otro')

            conexion.commit()

    return funcion_interna

#---------------------------------------------CRUD OPERATIONS
#------CREATE

@conectar
def crear_jugador(id_jugador, nombre, apellido):
        query = f"""INSERT INTO jugadores VALUES ('{id_jugador}', '{nombre}', '{apellido}')"""
        return query


@conectar
def crear_multiples_jugadores(lista_jugadores):
    query = "INSERT INTO jugadores ('id_jugador', 'nombre', 'apellido') VALUES (?, ?, ?)"
    jugadores = []
    for jugador in lista_jugadores:
        jugadores.append((jugador['id'], jugador['n'], jugador['a']))

    return query, jugadores

@conectar
def crear_registro_historico(fecha, retiro, idjugador, idpregunta, idopciones, idronda):
    query = f"""INSERT INTO historico VALUES ('{fecha}', '{retiro}', '{idjugador}', '{idpregunta}', '{idopciones}', '{idronda}')""" 
    return query

#------READ

@conectar
def mostrar_jugador(id_jugador):
    query = f"""SELECT * FROM jugadores WHERE  id_jugador = '{id_jugador}'"""
    return query

@conectar
def mostrar_preguntas_opciones_r(nivel):
    #query = f"""SELECT pr.texto_pregunta, op.texto_respuesta, op.veracidad FROM preguntas AS pr LEFT JOIN opciones AS op ON pr.id_preguntas = op.idpreguntas"""
    query = f"""SELECT 
                    pr.texto_pregunta,
                    op.texto_respuesta,
                    op.veracidad,
                    pr.id_preguntas,
                    op.id_opciones
                FROM preguntas AS pr
                LEFT JOIN opciones AS op 
                    ON pr.id_preguntas = op.idpreguntas
                WHERE pr.id_preguntas = (SELECT 
                    pr.id_preguntas
                 FROM 
                    preguntas AS pr 
                WHERE 
                    pr.idcategoria = '{nivel}'
                ORDER BY 
                    RANDOM() 
                LIMIT 1)"""
    return query

@conectar
def mostrar_acumulado_fecha(fecha, id_jugador):
    query = f"""SELECT 
                    premio 
                FROM rondaycategoria 
                WHERE 
                    id_ronda = 
                (SELECT
                    MAX(his.idronda) 
                FROM historico AS his
                INNER JOIN rondaycategoria AS ryc 
                    ON his.idronda = ryc.id_ronda
                WHERE
                    his.fecha = '{fecha}'
                    AND
                    his.idjugador = '{id_jugador}'
                    AND
                    his.retiro = 'False')
                    """
    return query
#------UPDATE


#------DELETE
