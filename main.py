import random

numero_secreto = random.randint(1,100)

def quem_comeca(nome_jogador):
    return random.choice([nome_jogador, "COMPUTADOR"])

def fazer_palpite_humano(palpites_jogador):
    palpite = int(input("Insira um valor entre 1 e 100: "))
    palpites_jogador.append(palpite)
    return palpite

def fazer_palpite_computador(palpites_computador):
    palpite = random.randint(1,100)
    palpites_computador.append(palpite)
    return palpite

def verificar_palpite(palpite, numero_secreto):
    if palpite == numero_secreto:
        return True
    elif palpite < numero_secreto:
        print("O número é maior que", palpite)
    else:
        print("O número é menor que", palpite)
    return False

palpites_jogador = []
palpites_computador = []

print("Bem vindo ao Jogo ADIVINHE O NÚMERO!")
nome_jogador = input("Por favor, digite seu nome: ").upper()

comeca_primeiro = quem_comeca(nome_jogador)
print(f"Sorteado para começa primeiro: {comeca_primeiro}")

while True:
    if comeca_primeiro == nome_jogador:
        print(f"\n----------------------- Sua Vez {nome_jogador} -----------------------")
        palpite = fazer_palpite_humano(palpites_jogador)
        if verificar_palpite(palpite, numero_secreto):
            print(f"Parabéns {nome_jogador}, você acertou! O número secreto era: {numero_secreto}")
            break
    else:
        print("\n----------------------- Vez do Computador -----------------------")
        palpite = fazer_palpite_computador(palpites_computador)
        if verificar_palpite(palpite, numero_secreto):
            print(f"A máquina venceu o jogo. O número secreto era {numero_secreto}")
            break

    if comeca_primeiro != nome_jogador:
        print(f"\n----------------------- Sua Vez {nome_jogador} -----------------------")
        palpite = fazer_palpite_humano(palpites_jogador)
        if verificar_palpite(palpite, numero_secreto):
            print(f"Parabéns {nome_jogador}, você acertou! O número secreto era: {numero_secreto}")
            break
    else:
        print("----------------------- Vez do Computador -----------------------")
        palpite = fazer_palpite_computador(palpites_computador)
        if verificar_palpite(palpite, numero_secreto):
            print(f"A máquina venceu o jogo. O número secreto era {numero_secreto}")
            break
        
print(f"Palpites do Jogador {nome_jogador}: {palpites_jogador}")
print(f"Palpites do Computador: {palpites_computador}")
