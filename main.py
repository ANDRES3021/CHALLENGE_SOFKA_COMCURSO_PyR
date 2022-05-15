#!/usr/bin/python3
"""Archivo que contiene el codigo de ejecucion del programa"""
from controlador import Controlador
from datetime import date

if __name__ == '__main__':

    fecha = str(date.today())
    c = Controlador()
    c.mostrar_bienvenida()
    documento = c.registrar()
    for nivel in range(1, 6):
    
        respuesta_secreta, id_pregunta, respuestas_id = c.mostrar_informacion_ronda(nivel)
        continuar = c.seguir_si_no()
        retiro = not continuar
        if retiro:
            c.guardar_registro_historico(fecha, retiro, documento, id_pregunta, None, nivel)
            c.mostrar_acumulado(fecha, documento)
            break
        acertado, id_respuesta = c.responder_pregunta(respuesta_secreta, respuestas_id)
        c.guardar_registro_historico(fecha, retiro, documento, id_pregunta, id_respuesta, nivel)
        equivocado = not acertado
        if equivocado:
            c.despedir_jugador()
            break

        if (nivel == 5) and acertado:
            c.felicitar_jugador()
            c.mostrar_acumulado(fecha, documento)
