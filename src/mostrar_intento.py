def mostrar_intento(numero_intento, cromosoma, pines):
    cromosoma_string = ' '.join(cromosoma)
    pines_string = ' '.join(pines)
    print('Intento ' + str(numero_intento) + ': ' + cromosoma_string + ' | ' + pines_string)