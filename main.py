import random

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

def fazer_palpite(nome_jogador, palpites_jogador, palpites_computador):
    if nome_jogador == "COMPUTADOR":
        return fazer_palpite_computador(palpites_computador)
    else:
        return fazer_palpite_humano(palpites_jogador)

def verificar_palpite(palpite, numero_secreto):
    if palpite == numero_secreto:
        return True
    elif palpite < numero_secreto:
        print("O número é maior que", palpite)
    else:
        print("O número é menor que", palpite)
    return False

def reiniciar_jogo():
    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
    if jogar_novamente == 's':
        return True
    else:
        jogar_novamente == 'n'
        return False

if __name__ == "__main__":

  while True:
    numero_secreto = random.randint(1,100)
    palpites_jogador = []
    palpites_computador = []

    print("Bem vindo ao Jogo ADIVINHE O NÚMERO!")
    nome_jogador = input("\nPor favor, digite seu nome: ").upper()

    comeca_primeiro = quem_comeca(nome_jogador)
    print(f"\nSorteado para começa primeiro: {comeca_primeiro}")

    while True:
        if comeca_primeiro == nome_jogador:
            print(f"\n----------------------- Sua Vez {nome_jogador} -----------------------")
            palpite = fazer_palpite(nome_jogador, palpites_jogador, palpites_computador)
            if verificar_palpite(palpite, numero_secreto):
                print(f"\nParabéns {nome_jogador}, você acertou! O número secreto era: {numero_secreto}")
                break
        else:
            print("\n----------------------- Vez do Computador -----------------------")
            palpite = fazer_palpite("COMPUTADOR", palpites_jogador, palpites_computador)
            if verificar_palpite(palpite, numero_secreto):
                print(f"\nA máquina venceu o jogo. O número secreto era: {numero_secreto}")
                break

        #operador ternário para alterar o valor de começa_primeiro para o computador, alterando a rodada
        comeca_primeiro = "COMPUTADOR" if comeca_primeiro == nome_jogador else nome_jogador

    print(f"\nPalpites do Jogador {nome_jogador}: {palpites_jogador}")
    print(f"Palpites do Computador: {palpites_computador}")

    if not reiniciar_jogo():
      print("\nObrigado por jogar! Até a próxima.")
      break
