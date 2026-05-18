"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
     # Cargar el archivo TSV
    df = pd.read_csv("files/input/tbl0.tsv", sep = "\t")
    variable = df.shape[0]

    return variable

Resultado = pregunta_01()
print("El resultado es: ", Resultado)