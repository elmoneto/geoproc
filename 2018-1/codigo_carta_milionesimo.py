import math


__author__ = "Elmo Neto"
__email__ = "elmo@inf.ufsm.br"


def carta_milionesimo(lat, lon):
    codigo_faixas = list("ABCDEFGHIJKLMNOPQRSTUV")
    if (lat > 0):
        cod_carta.append('N')
    else:
        cod_carta.append('S')

    cod_faixa = math.floor(abs(lat) / 4)
    cod_carta.append(codigo_faixas[cod_faixa])

    cod_fuso = math.ceil((lon + 180) / 6)
    cod_carta.append(cod_fuso)

    limite_inf_faixa = ((math.floor(lat / 4)) * 4) * 1.0
    limite_sup_faixa = ((math.ceil(lat / 4)) * 4) * 1.0
    limite_esq_fuso = ((math.floor(lon / 6)) * 6) * 1.0
    limite_dir_fuso = ((math.ceil(lon / 6)) * 6) * 1.0

    ponto_a = {'x': limite_esq_fuso, 'y': limite_inf_faixa}
    ponto_b = {'x': limite_esq_fuso, 'y': limite_sup_faixa}
    ponto_c = {'x': limite_dir_fuso, 'y': limite_sup_faixa}
    ponto_d = {'x': limite_dir_fuso, 'y': limite_inf_faixa}
    novos_pontos = {'pto_inf_esq': ponto_a, 'pto_sup_esq': ponto_b, 'pto_sup_dir': ponto_c, 'pto_inf_dir': ponto_d}
    return novos_pontos


def amplia_no(pto_medio_x, pto_medio_y, ptos):
    pto_a = {'x': ptos['pto_inf_esq']['x'], 'y': pto_medio_y}
    pto_b = ptos['pto_sup_esq']
    pto_c = {'x': pto_medio_x, 'y': ptos['pto_sup_dir']['y']}
    pto_d = {'x': pto_medio_x, 'y': pto_medio_y}
    novos_ptos = {'pto_inf_esq': pto_a, 'pto_sup_esq': pto_b, 'pto_sup_dir': pto_c, 'pto_inf_dir': pto_d}
    return novos_ptos


def amplia_ne(pto_medio_x, pto_medio_y, ptos):
    pto_a = {'x': pto_medio_x, 'y': pto_medio_y}
    pto_b = {'x': pto_medio_x, 'y': ptos['pto_sup_dir']['y']}
    pto_c = {'x': ptos['pto_sup_dir']['x'], 'y': ptos['pto_sup_dir']['y']}
    pto_d = {'x': ptos['pto_sup_dir']['x'], 'y': pto_medio_y}
    temp = {'pto_inf_esq': pto_a, 'pto_sup_esq': pto_b, 'pto_sup_dir': pto_c, 'pto_inf_dir': pto_d}
    return temp


def amplia_so(pto_medio_x, pto_medio_y, ptos):
    pto_a = {'x': ptos['pto_inf_esq']['x'], 'y': ptos['pto_inf_esq']['y']}
    pto_b = {'x': ptos['pto_inf_esq']['x'], 'y': pto_medio_y}
    pto_c = {'x': pto_medio_x, 'y': pto_medio_y}
    pto_d = {'x': pto_medio_x, 'y': ptos['pto_inf_esq']['y']}
    temp = {'pto_inf_esq': pto_a, 'pto_sup_esq': pto_b, 'pto_sup_dir': pto_c, 'pto_inf_dir': pto_d}
    return temp


def amplia_se(pto_medio_x, pto_medio_y, ptos):
    pto_a = {'x': pto_medio_x, 'y': ptos['pto_inf_dir']['y']}
    pto_b = {'x': pto_medio_x, 'y': pto_medio_y}
    pto_c = {'x': ptos['pto_inf_dir']['x'], 'y': pto_medio_y}
    pto_d = {'x': ptos['pto_inf_dir']['x'], 'y': ptos['pto_inf_dir']['y']}
    novos_ptos = {'pto_inf_esq': pto_a, 'pto_sup_esq': pto_b, 'pto_sup_dir': pto_c, 'pto_inf_dir': pto_d}
    return novos_ptos


def amplia_i(pmx1, pmy, pontos):
    pto_a = {'x': pontos['pto_inf_esq']['x'], 'y': pmy}
    pto_b = {'x': pontos['pto_sup_esq']['x'], 'y': pontos['pto_sup_esq']['y']}
    pto_c = {'x': pmx1, 'y': pontos['pto_sup_esq']['y']}
    pto_d = {'x': pmx1, 'y': pmy}
    novos_pontos = {'pto_inf_esq': pto_a, 'pto_sup_esq': pto_b, 'pto_sup_dir': pto_c, 'pto_inf_dir': pto_d}
    return novos_pontos


def amplia_ii(pmx1, pmx2, pmy, pontos):
    pto_a = {'x': pmx1, 'y': pmy}
    pto_b = {'x': pmx1, 'y': pontos['pto_sup_esq']['y']}
    pto_c = {'x': pmx2, 'y': pontos['pto_sup_esq']['y']}
    pto_d = {'x': pmx2, 'y': pmy}
    novos_pontos = {'pto_inf_esq': pto_a, 'pto_sup_esq': pto_b, 'pto_sup_dir': pto_c, 'pto_inf_dir': pto_d}
    return novos_pontos


def amplia_iii(pmx2, pmy, pontos):
    pto_a = {'x': pmx2, 'y': pmy}
    pto_b = {'x': pmx2, 'y': pontos['pto_sup_dir']['y']}
    pto_c = {'x': pontos['pto_sup_dir']['x'], 'y': pontos['pto_sup_dir']['y']}
    pto_d = {'x': pontos['pto_sup_dir']['x'], 'y': pmy}
    novos_pontos = {'pto_inf_esq': pto_a, 'pto_sup_esq': pto_b, 'pto_sup_dir': pto_c, 'pto_inf_dir': pto_d}
    return novos_pontos


def amplia_iv(pmx1, pmy, pontos):
    pto_a = {'x': pontos['pto_inf_esq']['x'], 'y': pontos['pto_inf_esq']['y']}
    pto_b = {'x': pontos['pto_inf_esq']['x'], 'y': pmy}
    pto_c = {'x': pmx1, 'y': pmy}
    pto_d = {'x': pmx1, 'y': pontos['pto_inf_esq']['y']}
    novos_pontos = {'pto_inf_esq': pto_a, 'pto_sup_esq': pto_b, 'pto_sup_dir': pto_c, 'pto_inf_dir': pto_d}
    return novos_pontos


def amplia_v(pmx1, pmx2, pmy, pontos):
    pto_a = {'x': pmx1, 'y': pontos['pto_inf_esq']['y']}
    pto_b = {'x': pmx1, 'y': pmy}
    pto_c = {'x': pmx2, 'y': pmy}
    pto_d = {'x': pmx2, 'y': pontos['pto_inf_esq']['y']}
    novos_pontos = {'pto_inf_esq': pto_a, 'pto_sup_esq': pto_b, 'pto_sup_dir': pto_c, 'pto_inf_dir': pto_d}
    return novos_pontos


def amplia_vi(pmx2,pmy,pontos):
    pto_a = {'x': pmx2, 'y': pontos['pto_inf_esq']['y']}
    pto_b = {'x': pmx2, 'y': pmy}
    pto_c = {'x': pontos['pto_sup_dir']['x'], 'y': pmy}
    pto_d = {'x': pontos['pto_inf_dir']['x'], 'y': pontos['pto_inf_dir']['y']}
    novos_pontos = {'pto_inf_esq': pto_a, 'pto_sup_esq': pto_b, 'pto_sup_dir': pto_c, 'pto_inf_dir': pto_d}
    return novos_pontos


def amplia_4reg(lat, lon, pontos, codigos):
    ponto_medio_x = (pontos['pto_inf_esq']['x'] + pontos['pto_inf_dir']['x']) / 2
    ponto_medio_y = (pontos['pto_inf_esq']['y'] + pontos['pto_sup_esq']['y']) / 2

    if (lat > ponto_medio_y) and (lon <= ponto_medio_x):
        cod_carta.append(codigos["NO"])
        novos_pontos = amplia_no(ponto_medio_x, ponto_medio_y, pontos)
        return novos_pontos

    if (lat > ponto_medio_y) and (lon > ponto_medio_x):
        cod_carta.append(codigos["NE"])
        novos_pontos = amplia_ne(ponto_medio_x, ponto_medio_y, pontos)
        return novos_pontos

    if (lat <= ponto_medio_y) and (lon <= ponto_medio_x):
        cod_carta.append(codigos["SO"])
        novos_pontos = amplia_so(ponto_medio_x, ponto_medio_y, pontos)
        return novos_pontos

    if (lat <= ponto_medio_y) and (lon > ponto_medio_x):
        cod_carta.append(codigos["SE"])
        novos_pontos = amplia_se(ponto_medio_x, ponto_medio_y, pontos)
        return novos_pontos


def amplia_6reg(lat, lon, pontos):
    temp = (pontos['pto_inf_dir']['x'] - pontos['pto_inf_esq']['x']) / 3
    pmx1 = pontos['pto_inf_esq']['x'] + temp
    pmx2 = pmx1 + temp
    pmy = (pontos['pto_inf_esq']['y'] + pontos['pto_sup_esq']['y']) / 2
    print(pmx1, pmx2, pmy)
    if (lat > pmy) and (lon <= pmx1):
        cod_carta.append("I")
        novos_pontos = amplia_i(pmx1, pmy, pontos)
        return novos_pontos
    if (lat > pmy) and (lon <= pmx2):
        cod_carta.append("II")
        novos_pontos = amplia_ii(pmx1, pmx2, pmy, pontos)
        return novos_pontos
    if (lat > pmy) and (lon > pmx2):
        cod_carta.append("III")
        novos_pontos = amplia_iii(pmx2, pmy, pontos)
        return novos_pontos
    if (lat <= pmy) and (lon <= pmx1):
        cod_carta.append("IV")
        novos_pontos = amplia_iv(pmx1, pmy, pontos)
        return novos_pontos
    if (lat <= pmy) and (lon <= pmx2):
        cod_carta.append("V")
        novos_pontos = amplia_v(pmx1, pmx2, pmy, pontos)
        return novos_pontos
    if (lat <= pmy) and (lon > pm2):
        cod_carta.append("VI")
        novos_pontos = amplia_vi(pmx2, pmy, pontos)
        return novos_pontos


lat = float(input("Informe a latitude: "))
lon = float(input("Informe a longitude: "))
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

if (nivel >= 1):
    pontos_limite = carta_milionesimo(lat, lon)
#    print(pontos_limite)
if (nivel >= 2):
    pontos_limite = amplia_4reg(lat, lon, pontos_limite, dicio_um_500_mil)
#    print(pontos_limite)
if (nivel >= 3):
    pontos_limite = amplia_4reg(lat, lon, pontos_limite, dicio_um_250_mil)
#    print(pontos_limite)
if (nivel >= 4):
    pontos_limite = amplia_6reg(lat, lon, pontos_limite)
#    print(pontos_limite)
if (nivel >= 5):
    pontos_limite = amplia_4reg(lat, lon, pontos_limite, dicio_um_50_mil)
#    print(pontos_limite)
if nivel == 6:
    pontos_limite = amplia_4reg(lat, lon, pontos_limite, dicio_um_25_mil)
    print(pontos_limite)
print(cod_carta)
