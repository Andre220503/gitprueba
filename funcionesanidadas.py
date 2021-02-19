def division(num_uno, num_dos):

    def validacion():
        return num_uno > 0 and num_dos > 0

    return num_uno / num_dos

resultado = division(10 , 2)
print(int(resultado))