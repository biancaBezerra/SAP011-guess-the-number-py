import random

limite_inferior = 1
limite_superior = 100
numero_secreto = random.randint(limite_inferior, limite_superior)

def quem_comeca(nome_jogador):
    return random.choice([nome_jogador, "COMPUTADOR"])

def fazer_palpite(limite_inferior, limite_superior, palpites):
    palpite = int(input("Insira um valor entre 1 e 100: "))
    palpites.append(palpite)
    return palpite

def verificar_palpite(palpite, numero_secreto):
    if palpite == numero_secreto:
        return True
    elif palpite < numero_secreto:
        print("O número é maior.")
    else:
        print("O número é menor.")
    return False

palpites_jogador = []
palpites_computador = []

print("Bem vindo ao Jogo ADIVINHE O NÚMERO!")
nome_jogador = input("Por favor, digite seu nome: ").upper()

comeca_primeiro = quem_comeca(nome_jogador)
print(f"Sorteado para começa primeiro: {comeca_primeiro}")

while True:
    if comeca_primeiro == nome_jogador:
        palpite = fazer_palpite(limite_inferior, limite_superior, palpites_jogador)
        if verificar_palpite(palpite, numero_secreto):
            print(f"Parabéns, {nome_jogador}, você acertou! O número secreto era: {numero_secreto}")
            break
    else:
        palpite = random.randint(limite_inferior, limite_superior)
        palpites_computador.append(palpite)
        if verificar_palpite(palpite, numero_secreto):
            print(f"A máquina venceu o jogo. O número secreto era {numero_secreto}")
            break

    if comeca_primeiro != nome_jogador:
        palpite = fazer_palpite(limite_inferior, limite_superior, palpites_jogador)
        if verificar_palpite(palpite, numero_secreto):
            print(f"Parabéns, {nome_jogador}, você acertou! O número secreto era: {numero_secreto}")
            break
    else:
        palpite = random.randint(limite_inferior, limite_superior)
        palpites_computador.append(palpite)
        if verificar_palpite(palpite, numero_secreto):
            print(f"A máquina venceu o jogo. O número secreto era {numero_secreto}")
            break

print(f"Palpites do Jogador {nome_jogador}: {palpites_jogador}")
print(f"Palpites do Computador: {palpites_computador}")

