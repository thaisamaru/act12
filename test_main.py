def test_multiplicar():
    response = client.get("/multiplicar/2/2")
    assert response.status_code == 200
    assert response.json() == {"resultado": 4} # Para a etapa 5 do exercício, altere 4 para 5 temporariamente para testar a falha no PR.