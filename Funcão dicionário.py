#def Subir(): #Função subir
#    print("case1") #Imprimi palavra

#def Descer(): #Função descer
#    print("case2") #Imprimi palavra


#while True:
#    Comando = { #Chaves abre o dicionário
#        0:Subir, # (Subir) pertence (:) ao numero (0)
#        1:Descer,# (Descer) pertence (:) ao numero (1)
#        }
#    Comando = Comando.get (int(input('Digite o numero 0 para "Subir" ou 1 para "Descer": '))) # (Comando.get) roda o dicionário aquisitando a palavra através do numero(0 ou 1) para a variável Comando.
#    Comando() #Roda a função escrita na variável Comando

print('CONTROLE DE ESTOQUE')
Matriz = [('Parafuso',10)]
Estoque = dict(Matriz)
 


while True:

    Fazer = int(input('Clique 0 para adionar, 1 para exluir e 2 para mostrar a lista: '))

    if (Fazer == 0):
        Peça = input('Digite o nome da peça: ')
        Quantidade = float(input('Digite o valor da peça: '))
        Estoque [Peça] = Quantidade
        print (Estoque)

    elif (Fazer == 1):
        Peça = input ('Digite a peça que você quer exluir: ')
        del Estoque.get [Peça]
        print (Estoque)
        
        
    else:
        print (Estoque)
    
        
    
