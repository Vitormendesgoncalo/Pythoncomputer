import time
Primo = int(input('Digite um numero que iremos dizer quantos numeros primos abaixo dele existem: ')) # Variável Primo aquisita um número que será limite
Divisor = int(1) # Numero inicial que irá dividir o numero e se o resto for 0 será contabilizado em uma variável Soma
Numero = int(2) # Sofrerá a divisão da variável Divisor
Soma = int(0) # Variável que começará com zero, mas irá somar cada vez que o resto der 0 da divisão

while Numero<=Primo: # Enquanto o numero for menor do que o valor aquisitado em primo executará a rotina abaixo 

    if Divisor<=Numero: # Enquanto o Divisor for menor do que o numero a ser dividido 
            Resultado = int (Numero%Divisor) # Pega o resto da divisão e armazena em resultado
            Divisor += 1 # Soma mais 1 no numero para fazer a próxima divisão
            if Resultado == 0: # Verifica se a divisão deu 0 mesmo
                Soma+=1 # Soma 1 na variável Soma
                
            
    else:
        if Soma == 2: # Se só somou 2 vezes é um numero primo
            print('O numero', Numero,'é primo') # mostra o numero primo
        Soma = 0 # Zera a soma 
        Numero += 1 # soma 1 no numero
        Divisor = 1 # joga novamente o valor inicial 1 no Divisor
        
    
