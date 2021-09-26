def Subir(): #Função subir

def Descer(): #Função descer
    print("case2") #Imprimi palavra


while True:
    Comando = { #Chaves abre o dicionário
        0:Subir, # (Subir) pertence (:) ao numero (0)
        1:Descer,# (Descer) pertence (:) ao numero (1)
        }
    Comando = Comando.get (int(input('Digite o numero 0 para "Subir" ou 1 para "Descer": '))) # (Comando.get) roda o dicionário aquisitando a palavra através do numero(0 ou 1) para a variável Comando.
    Comando() #Roda a função escrita na variável Comando
