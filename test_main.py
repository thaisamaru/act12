def test_multiplicar():
    response = client.get("/multiplicar/2/2")
    assert response.status_code == 200
    assert response.json() == {"resultado": 5} 
