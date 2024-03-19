from main import fazer_palpite_computador, quem_comeca

def test_quem_comeca(monkeypatch):
    # Simulando entrada do jogador
    nome_jogador = "Jogador"  # Simulando entrada do jogador

    # Definindo a entrada simulada/lambda cria um nome que seria digitado no input
    monkeypatch.setattr('builtins.input', lambda _: nome_jogador)

    assert quem_comeca(nome_jogador) in [nome_jogador, "COMPUTADOR"]

def test_fazer_palpite_computador():
    palpites_computador = []
    palpite = fazer_palpite_computador(palpites_computador)
    
    # Verifica se o palpite está dentro do intervalo de 1 a 100
    assert 1 <= palpite <= 100
    
    # Verifica se o palpite foi adicionado à lista de palpites do computador
    assert palpite in palpites_computador

