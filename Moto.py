print ("Vamos te fornecer dados referente a sua moto!")
def MOTO(Modelo, Ano, Combustivel):
    if Modelo == 'YAMAHA':
        if Ano == 2021:
            if Combustivel == 'GASOLINA':
                print("40km/l")
def CARRO(Modelo, Ano, Combustivel):
    print("Carro")
def CAMINHÃO(Modelo, Ano, Combustivel):
    print("Caminhão")
while True:
    Veiculo = str(input("Digite se seu veículo é moto, carro ou caminhão: ")).strip().upper()
    Modelo = str(input("Digite o modelo do seu veículo")).strip().upper()
    Ano = int(input("Digite o ano do seu veículo"))
    Combustivel = str(input("Digite o combustível do seu veículo")).strip().upper()
    if Veiculo == 'MOTO':
        MOTO(Modelo, Ano, Combustivel)
    elif Veiculo == 'CARRO':
        CARRO(Modelo, Ano, Combustivel)
    elif Veiculo == 'CARRO':
        CAMINHÃO(Modelo, Ano, Combustivel)