import nltk
from nltk.sem.logic import Expression

#Inicializar al analizador
read_expr =Expression.fromstring
# Definir las constantes para migdalia, Julissa, Daniel
migdalia = read_expr('migdalia')
Julissa =read_expr('Julissa')
Daniel = read_expr('Daniel')

#Definir los predicados con las constantes
amigos_migdalia_Julissa = read_expr('amigos(migdalia,julissa)')
amigos_migdalia_Daniel = read_expr('no_son_amigos(migdalia, Daniel)')
no_amigos_Daniel_Julissa = read_expr('tienen_la_misma_edad(Daniel, Julissa)')
trabajan_juntos_migdalia_Julissa = read_expr('trabajan(migdalia,Julissa)')

#Crear un conjunto de formulas
formulas = [
    amigos_migdalia_Julissa,
    amigos_migdalia_Daniel,
    no_amigos_Daniel_Julissa,
    trabajan_juntos_migdalia_Julissa
]
#Imprimir las formulas
for formula in formulas:
    print(f"{formula}: {formula}")