"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    suma = 0
    with open('data.csv', 'r') as file:
        for line in file:
            columns = line.split()
            if len(columns) >= 2:
                suma += int(columns[1])
    return suma



def pregunta_02():
    registros_por_letra = {}
    with open('data.csv', 'r') as file:
        for line in file:
            columns = line.split()
            if len(columns) >= 1:
                letra = columns[0]
                registros_por_letra[letra] = registros_por_letra.get(letra, 0) + 1

    lista_resultado = sorted(registros_por_letra.items())

    return lista_resultado


def pregunta_03():
    suma_por_letra = {}
    with open('data.csv', 'r') as file:
        for line in file:
            columns = line.split()
            if len(columns) >= 2:
                letra = columns[0]
                valor = int(columns[1])
                suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor

    lista_resultado = sorted(suma_por_letra.items())

    return lista_resultado

def pregunta_04():
    registros_por_mes = {}
    with open('data.csv', 'r') as file:
        for line in file:
            columns = line.split()
            if len(columns) >= 3:
                fecha = columns[2]
                mes = fecha.split("-")[1]
                registros_por_mes[mes] = registros_por_mes.get(mes, 0) + 1

    lista_resultado = sorted(registros_por_mes.items())

    return lista_resultado


def pregunta_05():
    valores_extremos = {}
    with open('data.csv', 'r') as file:
        for line in file:
            columns = line.split()
            if len(columns) >= 2:
                letra = columns[0]
                valor = int(columns[1])
                if letra not in valores_extremos:
                    valores_extremos[letra] = (valor, valor)
                else:
                    minimo_actual, maximo_actual = valores_extremos[letra]
                    valores_extremos[letra] = (min(minimo_actual, valor), max(maximo_actual, valor))

    lista_resultado = [(letra, valores_extremos[letra][1], valores_extremos[letra][0]) for letra in sorted(valores_extremos)]

    return lista_resultado


def pregunta_06():
    valores_extremos = {}
    with open('data.csv', 'r') as file:
        for line in file:
            columns = line.split()
            if len(columns) >= 5:
                diccionario_codificado = columns[4]
                diccionario = {}
                pares = diccionario_codificado.split(",")
                for par in pares:
                    clave, valor = par.split(":")
                    diccionario[clave] = int(valor)
                for clave, valor in diccionario.items():
                    if clave not in valores_extremos:
                        valores_extremos[clave] = (valor, valor)
                    else:
                        minimo_actual, maximo_actual = valores_extremos[clave]
                        valores_extremos[clave] = (min(minimo_actual, valor), max(maximo_actual, valor))

    lista_resultado = [(clave, valores_extremos[clave][0], valores_extremos[clave][1]) for clave in sorted(valores_extremos)]

    return lista_resultado


def pregunta_07():
    asociaciones = {}
    with open('data.csv', 'r') as file:
        for line in file:
            columns = line.split()
            if len(columns) >= 2:
                valor_columna_2 = int(columns[1])
                letra_columna_1 = columns[0]
                if valor_columna_2 not in asociaciones:
                    asociaciones[valor_columna_2] = [letra_columna_1]
                else:
                    asociaciones[valor_columna_2].append(letra_columna_1)

    lista_resultado = [(valor, letras) for valor, letras in sorted(asociaciones.items())]

    return lista_resultado

def pregunta_08():
    asociaciones = {}
    with open('data.csv', 'r') as file:
        for line in file:
            columns = line.split()
            if len(columns) >= 2:
                valor_columna_2 = int(columns[1])
                letra_columna_1 = columns[0]
                if valor_columna_2 not in asociaciones:
                    asociaciones[valor_columna_2] = [letra_columna_1]
                else:
                    asociaciones[valor_columna_2].append(letra_columna_1)

    lista_resultado = [(valor, sorted(list(set(letras)))) for valor, letras in sorted(asociaciones.items())]

    return lista_resultado

def pregunta_09():
    cantidad_registros = {}
    with open('data.csv', 'r') as file:
        for line in file:
            columns = line.split()
            if len(columns) >= 5:
                diccionario_codificado = columns[4]
                pares = diccionario_codificado.split(",")
                for par in pares:
                    clave = par.split(":")[0]
                    if clave not in cantidad_registros:
                        cantidad_registros[clave] = 1
                    else:
                        cantidad_registros[clave] += 1

    
    cantidad_registros_ordenados = {clave: cantidad_registros[clave] for clave in sorted(cantidad_registros)}

    return cantidad_registros_ordenados


def pregunta_10():
    lista_tuplas = []
    with open('data.csv', 'r') as file:
        for line in file:
            columns = line.split()
            if len(columns) >= 5:
                letra_columna_1 = columns[0]
                cantidad_columnas_4 = len(columns[3].split(","))
                cantidad_columnas_5 = len(columns[4].split(","))
                tupla = (letra_columna_1, cantidad_columnas_4, cantidad_columnas_5)
                lista_tuplas.append(tupla)

    return lista_tuplas


def pregunta_11():
    suma_columna_2 = {}
    with open('data.csv', 'r') as file:
        for line in file:
            columns = line.split()
            if len(columns) >= 4:
                letras_columna_4 = set(columns[3])
                valor_columna_2 = int(columns[1])
                for letra in letras_columna_4:
                    if letra not in suma_columna_2:
                        suma_columna_2[letra] = valor_columna_2
                    else:
                        suma_columna_2[letra] += valor_columna_2

    suma_columna_2_ordenada = {letra: suma_columna_2[letra] for letra in sorted(suma_columna_2) if letra != ','}

    return suma_columna_2_ordenada


def pregunta_12():
    suma_columna_5 = {}
    with open('data.csv', 'r') as file:
        for line in file:
            columns = line.split()
            if len(columns) >= 5:
                clave_columna_1 = columns[0]
                valores_columna_5 = columns[4].split(',')
                for valor in valores_columna_5:
                    clave_valor = valor.split(':')
                    if len(clave_valor) == 2:
                        clave = clave_valor[0]
                        if clave_columna_1 not in suma_columna_5:
                            suma_columna_5[clave_columna_1] = int(clave_valor[1])
                        else:
                            suma_columna_5[clave_columna_1] += int(clave_valor[1])

    suma_columna_5_ordenada = dict(sorted(suma_columna_5.items()))

    return suma_columna_5_ordenada
