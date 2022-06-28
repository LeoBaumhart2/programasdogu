from Cardapio import *
from time import sleep
n10 = 'R$30,99'
n11 = 'R$32,69'
n12 = 'R$29,99'
n13 = 'R$30,99'
menu = input ('eae chefia, qual a boa do dia ? vai um menuzinho ai ?? ').upper()

if menu == 'SIM':
    print('Ta aqui chefe ')
    print(f'O que quer ? {pizzas} ')
    n3 = input('Qual vai ser ?')

else:
    print('Então cai fora irmão')
    sleep(1.0)
    print('Tenho mais o que fazer, tipo dormir o dia inteiro e estrangular uns alunos')


if menu == 'Sim' and n3 == 'Frango':
    print('Ta aqui chefia, R$30,99')
    sleep(1.7)
    print('Passa a grana ou o baguio vai ficar sério ...')

elif menu == 'Sim' and n3 == 'Requeijão':
    print('Ta aqui chefia, R$32,69')
    sleep(1.7)
    print('Passa a grana ou o baguio vai ficar sério ...')

elif menu == 'Sim' and n3 == 'Calabresa':
    print('Ta aqui chefia, R$29,99')
    sleep(1.8)
    print('Passa a grana ou o baguio vai ficar sério ...')

elif menu == 'Sim' and n3 == 'Bauru' and 'Mussarela':
    print('Ta aqui chefia, R$30,99')
    sleep(1.9)
    print('Passa a grana ou o baguio vai ficar sério ...')

menu2 = input('Tudo bem meu caro, vai UNA COKITA GELADINHA ??').upper()

if menu2 == 'Não':
    print('Espero que se engasgue, nojento ...')

elif menu2 == 'quero pepsi':
    print('Claro, bem melhor que coca, COFF ... COF ...')

else:
    print('R$6 Dols chefia pegar ou largar')

print('pegue seu pedido e caia fora')



