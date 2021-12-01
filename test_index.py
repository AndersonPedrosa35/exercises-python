import index

def testando_se_retorna_4_passando_2():
    "Testa se retorna valor 4 passando como parametro 2"
    assert index.square(2) is 4

def testando_a_função_rectangle_se_retorna_6_passando_3_e_2():
    "Testa se retorna o valor da area do retangulo como 4 passando 3 e 2 como parametro"
    assert index.rectangle(3, 2) is 6

def testando_a_função_circle_se_retorna_5024_passando_4():
    "Testa se retorna o valor da area do circulo como 50.24 passando 4"
    assert index.circle(3.57) is 40