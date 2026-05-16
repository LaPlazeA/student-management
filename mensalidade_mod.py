def calcular_mensalidade(cursos, turno, idade):

    total = 0

    for curso in cursos:

        if curso == 1:
            if turno == 1:
                total += 210
            else:
                total += 260

        elif curso == 2:
            if turno == 1:
                total += 320
            else:
                total += 390

        elif curso == 3:
            if turno == 1:
                total += 290
            else:
                total += 310

    desconto = 0

    if len(cursos) > 1:
        desconto = 0.30

    elif idade > 45:
        desconto = 0.15

    total = total - (total * desconto)

    return total