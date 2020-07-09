# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:55:03 2020

@author: Rhisto
"""
def determinaraprobado(promedio):
    if promedio <= 11:
        resultado = "Aprobado"
    else:
        resultado = "Desaprobado"
    return resultado
print(determinaraprobado(15))