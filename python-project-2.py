valorTotal = 0   # iniciando a variável com 0
op2 = 's'   # para não dar erro no if op2, como sera o primeiro pedido então ele recebera 's'

print('Bem-vindo a Sorveteria do Gabriel Peixoto de Campos')   # mensagem de boas-vindas

# início do cardápio / menu de opções

print('-' * 38 + 'Cardápio' + '-' * 38)

print('| N° DE BOLAS | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es)  |')

print('|' + ' ' * 6 + '1' + ' ' * 6 +   # coluna 1 linha 2
      '|' + ' ' * 9 + 'R$6,00' + ' ' * 9 +   # coluna 2 linha 2
      '|' + ' ' * 6 + 'R$7,00' + ' ' * 8 +   # coluna 3 linha 2
      '|' + ' ' * 8 + 'R$8,00' + ' ' * 8 + '|')   # coluna 4 linha 2

print('|' + ' ' * 6 + '2' + ' ' * 6 +   # coluna 1 linha 3
      '|' + ' ' * 9 + 'R$10,00' + ' ' * 8 +   # coluna 2 linha 3
      '|' + ' ' * 6 + 'R$12,00' + ' ' * 7 +   # coluna 3 linha 3
      '|' + ' ' * 8 + 'R$14,00' + ' ' * 7 + '|')   # coluna 4 linha 3

print('|' + ' ' * 6 + '3' + ' ' * 6 +   # coluna 1 linha 4
      '|' + ' ' * 9 + 'R$14,00' + ' ' * 8 +   # coluna 2 linha 4
      '|' + ' ' * 6 + 'R$17,00' + ' ' * 7 +   # coluna 3 linha 4
      '|' + ' ' * 8 + 'R$20,00' + ' ' * 7 + '|')   # coluna 4 linha 4

print('-' * 42 + '-' * 42)

# fim do cardápio / menu de opções



while True:
    if(op2 == 's'):   # se for true ele vai fazer o pedido, se não ele mostra o valor total e encerra o programa
        op = input('\nEntre com o sabor desejado (tr/es/pr): ')

        if(op == 'tr' or op == 'es' or op == 'pr'):

            # operação para sorvete tradicional
            if(op == 'tr'):
                sabor = 'TRADICIONAL'   # recebe o sabor do sorvete
                numBolas = int(input('Entre com o número de bolas de sorvete desejado (1/2/3): '))

                if(numBolas == 1): valorAtual = 6   # variável recebe o valor do sorvete com 1 bola
                elif(numBolas == 2): valorAtual = 10   # variável recebe o valor do sorvete com 2 bolas
                elif(numBolas == 3): valorAtual = 14   # variável recebe o valor do sorvete com 3 bolas
                else:
                    print('Número de bolas de sorvete inválido. Tente novamente')
                    continue



            # operação para sorvete premium
            elif(op == 'pr'):
                sabor = 'PREMIUM'   # recebe o sabor do sorvete
                numBolas = int(input('Entre com o número de bolas de sorvete desejado (1/2/3): '))

                if (numBolas == 1): valorAtual = 7   # variável recebe o valor do sorvete com 1 bola
                elif (numBolas == 2): valorAtual = 12   # variável recebe o valor do sorvete com 2 bolas
                elif (numBolas == 3): valorAtual = 17   # variável recebe o valor do sorvete com 3 bolas
                else:
                    numBolas = (print('Número de bolas de sorvete inválido. Tente novamente'))
                    continue



            # operação para sorvete especial
            elif(op == 'es'):
                sabor = 'ESPECIAL'   # recebe o sabor do sorvete
                numBolas = int(input('Entre com o número de bolas de sorvete desejado (1/2/3): '))

                if (numBolas == 1): valorAtual = 8   # variável recebe o valor do sorvete com 1 bola
                elif (numBolas == 2): valorAtual = 14   # variável recebe o valor do sorvete com 2 bolas
                elif (numBolas == 3): valorAtual = 20   # variável recebe o valor do sorvete com 3 bolas
                else:
                    numBolas = (print('Número de bolas de sorvete inválido. Tente novamente: '))
                    continue



            print('Você pediu {} bola(s) de sorvete no sabor {}: R${},00'.format(numBolas, sabor, valorAtual))

            # se for 's' o programa vai fazer outra compra, se for qualquer outra tecla o programa vai mostrar o total e depois será encerrado
            op2 = input('\nDeseja mais algum sorvete? (s / qualquer tecla para encerrar): ')

            valorTotal += valorAtual

        else:
            print('Sabor inválido. Tente novamente')

    else:
        print('\nO valor total a ser pago: R${},00'.format(valorTotal))
        break