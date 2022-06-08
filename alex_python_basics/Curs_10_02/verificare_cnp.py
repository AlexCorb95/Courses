

def verificare_cnp (cnp):
    cnp_control = "279146358279"
    suma = 0
    for index in range(12):
        cifra_cnp = cnp[index]
        cifra_control = cnp_control[index]
        suma = suma + int(cifra_control) * int(cifra_cnp)
    rest = suma % 11
    if rest == 10:
        control = 1
    else:
        control = rest
    print(int(cnp[-1]) == control)
    print(f"Suma este {suma}, restul este {rest}, cifra de control este {control}")


verificare_cnp("2970215018111")