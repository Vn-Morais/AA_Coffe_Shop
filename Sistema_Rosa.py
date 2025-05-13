massa_folhada = 10
ovo = 30
manteiga = 11
cafe_moido = 500
leite = 1000
pao_de_forma = 50
presunto = 50
queijo = 50
chocolate_em_po = 500
massa_de_biscoito = 15
leite_condensado = 100
limao_suco = 500
chantilly = 500

def card_disp():
    if nome != "":
        print(f"Bem vindo, {nome}! Aqui estão os itens disponíveis no momento:\n")
    else:
        print("Bem vindo! Aqui estão os itens disponíveis no momento:\n")

    if massa_folhada >= 1 and ovo >= 1 and manteiga >= 10:
        print("Croissant")
    else:
       print("Croissant - Fora de estoque"),

    if cafe_moido >= 10:
        print("Expresso")
    else:
       print("Expresso - Fora de estoque"),

    if cafe_moido >= 10 and leite >= 150:
        print("Latte")
    else:
       print("Latte - Fora de estoque")

    if pao_de_forma >= 2 and presunto >= 1 and queijo >= 1 and manteiga >= 5:
        print("Misto Quente")
    else:
       print("Misto Quente - Fora de estoque"),

    if chocolate_em_po >= 5 and cafe_moido >= 10 and leite >= 100:
        print("Capuccino")
    else:
       print("Capuccino - Fora de estoque")

    if massa_de_biscoito >= 1 and leite_condensado >= 50 and limao_suco >= 10 and chantilly >= 10:
        print("Torta de Limão")
    else:
       print("Torta de Limão - Fora de estoque")

verif = input("Deseja fazer o pedido com cadastro?\nDigite sim ou não ")
if verif == "Sim" or "sim":
    cpf = input("Digite seu CPF ")
    nome = input("Digite seu Nome ")
else:
    print("não")
card_disp()