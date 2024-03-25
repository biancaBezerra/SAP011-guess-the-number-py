from main import palpite_computador, quem_comeca, palpite_humano, verificar_palpite

def test_quem_comeca(monkeypatch): ##esse teste aqui é opcional, pois o choice ja foi testado
    # Simulando entrada do jogador
    nome_jogador = "Jogador"  # Simulando entrada do jogador

    # Definindo a entrada simulada/lambda cria um nome que seria digitado no input
    monkeypatch.setattr('builtins.input', lambda _: nome_jogador)

    assert quem_comeca(nome_jogador) in [nome_jogador, "COMPUTADOR"]

def test_palpite_humano(monkeypatch):
    palpites_jogador = []
    entrada = 10
    monkeypatch.setattr('builtins.input', lambda _: entrada)
    assert palpite_humano(palpites_jogador) == entrada
    assert entrada in palpites_jogador

def test_palpite_computador():
    palpites_computador = []
    palpite = palpite_computador(palpites_computador)
    # Verifica se o palpite está dentro do intervalo de 1 a 100
    assert 1 <= palpite <= 100
    # Verifica se o palpite foi adicionado à lista de palpites do computador
    assert palpite in palpites_computador

def test_verificar_palpite():
    #caso o palpite seja igual ao numero secreto retorna true
    assert verificar_palpite(40, 40) == True

    #caso o palpite seja menor que o numero secreto
    assert verificar_palpite(25, 40) == False

    #caso o palpite seja maior que o numero secreto
    assert verificar_palpite(50,40) == False
