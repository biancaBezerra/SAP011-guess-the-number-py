from main import fazer_palpite_computador, quem_comeca, fazer_palpite_humano, fazer_palpite, verificar_palpite, reiniciar_jogo

def test_quem_comeca(monkeypatch):
    # Simulando entrada do jogador
    nome_jogador = "Jogador"  # Simulando entrada do jogador

    # Definindo a entrada simulada/lambda cria um nome que seria digitado no input
    monkeypatch.setattr('builtins.input', lambda _: nome_jogador)

    assert quem_comeca(nome_jogador) in [nome_jogador, "COMPUTADOR"]

def test_fazer_palpite_humano(monkeypatch):
    palpites_jogador = []
    entrada = "10"
    monkeypatch.setattr('builtins.input', lambda _: entrada)
    assert fazer_palpite_humano(palpites_jogador) == int (entrada)

def test_fazer_palpite_computador():
    palpites_computador = []
    palpite = fazer_palpite_computador(palpites_computador)
    
    # Verifica se o palpite está dentro do intervalo de 1 a 100
    assert 1 <= palpite <= 100
    
    # Verifica se o palpite foi adicionado à lista de palpites do computador
    assert palpite in palpites_computador


def test_fazer_palpite(monkeypatch):
    palpites_jogador = []
    palpites_computador = []

    # Teste para o jogador humano
    entrada = "10"
    monkeypatch.setattr('builtins.input', lambda _: entrada)
    assert fazer_palpite("HUMANO", palpites_jogador, palpites_computador) == int(entrada)
    assert palpites_jogador == [int(entrada)]

    # Teste para o jogador computador
    palpite_computador = fazer_palpite("COMPUTADOR", palpites_jogador, palpites_computador)
    assert 1 <= palpite_computador <= 100
    assert palpite_computador in palpites_computador

def test_verificar_palpite():
    #caso o palpite seja igual ao numero secreto retorna true
    assert verificar_palpite(40, 40) == True

    #caso o palpite seja menor que o numero secreto
    assert verificar_palpite(25, 40) == False

    #caso o palpite seja maior que o numero secreto
    assert verificar_palpite(50,40) == False

def test_reiniciar_jogo_sim(monkeypatch):
    #caso o jogador queira jogar novamente
    jogar_novamente = "s"
    monkeypatch.setattr('builtins.input', lambda _: jogar_novamente)
    assert reiniciar_jogo() == True

def test_reiniciar_jogo_nao(monkeypatch):
    #caso o jogador queira parar o jogo
    jogar_novamente = "n"
    monkeypatch.setattr('builtins.input', lambda _: jogar_novamente)
    assert reiniciar_jogo() == False

