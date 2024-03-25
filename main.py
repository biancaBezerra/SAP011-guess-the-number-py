"""
Este módulo contém o jogo Guess The Number
Onde o jogador tenta adivinha um numero
"""
import random


def quem_comeca(nome_jogador):
    """
    Escolhe através de sorteio quem começa o jogo.
    """
    #isso é uma tupla(tuple)
    return random.choice((nome_jogador, "COMPUTADOR"))

def palpite_humano(palpites_jogador):
    """
    Função para obter um palpite de um jogador humano.
    """
    while True:
        palpite = int(input("Insira um valor entre 1 e 100: "))
        if 1 <= palpite <= 100:
            palpites_jogador.append(palpite)
            return palpite
        print("Por favor, insira um número dentro do intervalo de 1 a 100.")

def palpite_computador(palpites_computador):
    """
    Função para obter um palpite do computador.
    """
    palpite = random.randint(1,100)
    palpites_computador.append(palpite)
    return palpite

def fazer_palpite(nome_jogador, palpites_jogador, palpites_computador):
    """
    Função para fazer um palpite, dependendo do jogador.
    """
    if nome_jogador == "COMPUTADOR":
        return palpite_computador(palpites_computador)
    return palpite_humano(palpites_jogador)

def verificar_palpite(palpite, numero_secreto):
    """
    Função para verificar o palpite com o número secreto.
    """
    if palpite == numero_secreto:
        return True
    if palpite < numero_secreto:
        print("O número é maior que", palpite)
    else:
        print("O número é menor que", palpite)
    return False

def reiniciar_jogo():
    """
    Função para perguntar ao jogador se deseja jogar novamente.
    """
    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
    return jogar_novamente == 's'


def main():
    """
    Função principal para iniciar o jogo
    """
    while True:
        numero_secreto = random.randint(1,100)
        palpites_jogador = []
        palpites_computador = []

        print("Bem vindo ao Jogo ADIVINHE O NÚMERO!")
        nome_jogador = input("\nPor favor, digite seu nome: ").upper()

        #armazena retorno da função quem começa e printa o sorteado para começar
        primeiro_a_jogar = quem_comeca(nome_jogador)
        turno_computador = primeiro_a_jogar == "COMPUTADOR"
        print(f"\nSorteado para começa primeiro: {primeiro_a_jogar}")

        while True:
            if not turno_computador:
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

            #computador, alterando a rodada
            turno_computador = not turno_computador

        print(f"\nPalpites do Jogador {nome_jogador}: {palpites_jogador}")
        print(f"Palpites do Computador: {palpites_computador}")

        if not reiniciar_jogo():
            print("\nObrigado por jogar! Até a próxima.")
            break
        
#verifica se o nome do script atual é main e chama o while
if __name__ == "__main__":
    main()
