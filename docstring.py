def generador(*args):
    for valor in args:
        yield valor, True if valor > 5 else False






documentacion = generador.__doc__