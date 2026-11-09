# act12
Ao alterar a função em main.py de a + b para a - b:   Mensagem exata de erro que imprimiu:

assert response.json() == {"resultado": 8}
AssertionError: assert {'resultado': 2} == {'resultado': 8}
Differing items:
{'resultado': 2} != {'resultado': 8}

O que esperava receber e o que ele recebeu:
Esperava receber: {"resultado": 8} (foi $5 + 3 = 8$).
Recebeu de fato: {"resultado": 2} (foi $5 - 3 = 2$). 
