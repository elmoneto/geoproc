import math

__author__ = "Elmo Neto"
__email__ = "elmo@inf.ufsm.br"


def carta_milionesimo(arglat, arglon):
    codigo_faixas = list("ABCDEFGHIJKLMNOPQRSTUV")
    if arglat >= 0:
        cod_carta.append('N')
    else:
        cod_carta.append('S')

    cod_faixa = math.floor(abs(arglat) / 4)
    if arglat < 0 and arglat % 4 == 0 :
        cod_faixa -= 1
    cod_carta.append(codigo_faixas[cod_faixa])

    cod_fuso = (math.ceil((arglon + 180) / 6)) % 60
    if arglon % 6 == 0:
        cod_fuso += 1
    cod_carta.append(cod_fuso)

    limite_inf_faixa = ((math.floor(arglat / 4)) * 4) * 1.0
    limite_sup_faixa = limite_inf_faixa + 4
    limite_esq_fuso = ((math.floor(arglon / 6)) * 6) * 1.0
    limite_dir_fuso = limite_esq_fuso + 6

    ponto_a = {'x': limite_esq_fuso, 'y': limite_inf_faixa}
    ponto_b = {'x': limite_esq_fuso, 'y': limite_sup_faixa}
    ponto_c = {'x': limite_dir_fuso, 'y': limite_sup_faixa}
    ponto_d = {'x': limite_dir_fuso, 'y': limite_inf_faixa}
    novos_pontos = {'pto_inf_esq': ponto_a, 'pto_sup_esq': ponto_b, 'pto_sup_dir': ponto_c, 'pto_inf_dir': ponto_d}
    return novos_pontos


def amplia(linhax1, linhay1, linhax2, linhay2):
    ponto_a = {'x': linhax1, 'y': linhay1}
    ponto_b = {'x': linhax1, 'y': linhay2}
    ponto_c = {'x': linhax2, 'y': linhay2}
    ponto_d = {'x': linhax2, 'y': linhay1}
    novos_pontos = {'pto_inf_esq': ponto_a, 'pto_sup_esq': ponto_b, 'pto_sup_dir': ponto_c, 'pto_inf_dir': ponto_d}
    return novos_pontos


def amplia_4reg(arglat, arglon, pontos, codigos):
    ponto_medio_x = (pontos['pto_inf_esq']['x'] + pontos['pto_inf_dir']['x']) / 2
    ponto_medio_y = (pontos['pto_inf_esq']['y'] + pontos['pto_sup_esq']['y']) / 2

    if (arglat >= ponto_medio_y) and (arglon < ponto_medio_x):
        cod_carta.append(codigos["NO"])
        novos_pontos = amplia(pontos['pto_inf_esq']['x'], ponto_medio_y, ponto_medio_x, pontos['pto_sup_esq']['y'])
        return novos_pontos

    if (arglat >= ponto_medio_y) and (arglon >= ponto_medio_x):
        cod_carta.append(codigos["NE"])
        novos_pontos = amplia(ponto_medio_x, ponto_medio_y, pontos['pto_sup_dir']['x'], pontos['pto_sup_dir']['y'])
        return novos_pontos

    if (arglat < ponto_medio_y) and (arglon < ponto_medio_x):
        cod_carta.append(codigos["SO"])
        novos_pontos = amplia(pontos['pto_inf_esq']['x'], pontos['pto_inf_esq']['y'], ponto_medio_x, ponto_medio_y)
        return novos_pontos

    if (arglat < ponto_medio_y) and (arglon >= ponto_medio_x):
        cod_carta.append(codigos["SE"])
        novos_pontos = amplia(ponto_medio_x, pontos['pto_inf_esq']['y'], pontos['pto_inf_dir']['x'], ponto_medio_y)
        return novos_pontos


def amplia_6reg(arglat, arglon, pontos):
    temp = (pontos['pto_inf_dir']['x'] - pontos['pto_inf_esq']['x']) / 3
    pmx1 = pontos['pto_inf_esq']['x'] + temp
    pmx2 = pmx1 + temp
    pmy = (pontos['pto_inf_esq']['y'] + pontos['pto_sup_esq']['y']) / 2
    if (arglat >= pmy) and (arglon < pmx1):
        cod_carta.append("I")
        novos_pontos = amplia(pontos['pto_sup_esq']['x'], pmy, pmx1, pontos['pto_sup_esq']['y'])
        return novos_pontos
    if (arglat >= pmy) and (arglon < pmx2):
        cod_carta.append("II")
        novos_pontos = amplia(pmx1, pmy, pmx2, pontos['pto_sup_esq']['y'])
        return novos_pontos
    if (arglat >= pmy) and (arglon >= pmx2):
        cod_carta.append("III")
        novos_pontos = amplia(pmx2, pmy, pontos['pto_sup_dir']['x'], pontos['pto_sup_dir']['y'])
        return novos_pontos
    if (arglat < pmy) and (arglon < pmx1):
        cod_carta.append("IV")
        novos_pontos = amplia(pontos['pto_inf_esq']['x'], pontos['pto_inf_esq']['y'], pmx1, pmy)
        return novos_pontos
    if (arglat < pmy) and (arglon < pmx2):
        cod_carta.append("V")
        novos_pontos = amplia(pmx1, pontos['pto_inf_esq']['y'], pmx2, pmy)
        return novos_pontos
    if (arglat < pmy) and (arglon >= pmx2):
        cod_carta.append("VI")
        novos_pontos = amplia(pmx2, pontos['pto_inf_esq']['y'], pontos['pto_inf_dir']['x'], pmy)
        return novos_pontos


lat = float(input("Latitude (em formato decimal): "))
lon = float(input("Longitude (em formato decimal): "))
pontos_limite = {}
dicio_um_500_mil = {"NO": "V", "NE": 'X', "SO": 'Y', "SE": "Z"}
dicio_um_250_mil = {"NO": "A", "NE": "B", "SO": "C", "SE": "D"}
dicio_um_50_mil = {"NO": 1, "NE": 2, "SO": 3, "SE": 4}
dicio_um_25_mil = {"NO": "NO", "NE": "NE", "SO": "SO", "SE": "SE"}

cod_carta = []

print("Informe a escala da carta desejada: ")
print("(1) - 1:1.000.000")
print("(2) - 1:500.000")
print("(3) - 1:250.000")
print("(4) - 1:100.000")
print("(5) - 1:50.000")
print("(6) - 1:25:000")
nivel = int(input(""))

if nivel >= 1:
    pontos_limite = carta_milionesimo(lat, lon)
#    print(pontos_limite)
if nivel >= 2:
    pontos_limite = amplia_4reg(lat, lon, pontos_limite, dicio_um_500_mil)
#    print(pontos_limite)
if nivel >= 3:
    pontos_limite = amplia_4reg(lat, lon, pontos_limite, dicio_um_250_mil)
#    print(pontos_limite)
if nivel >= 4:
    pontos_limite = amplia_6reg(lat, lon, pontos_limite)
#    print(pontos_limite)
if nivel >= 5:
    pontos_limite = amplia_4reg(lat, lon, pontos_limite, dicio_um_50_mil)
#    print(pontos_limite)
if nivel == 6:
    pontos_limite = amplia_4reg(lat, lon, pontos_limite, dicio_um_25_mil)
    print(pontos_limite)
print("\nCódigo da carta: ")
print(cod_carta)
