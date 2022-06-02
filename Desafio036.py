valor = float(input('Qual o valor do empréstimo? R$  '))
salario = float(input('Qual é o seu salário? R$ '))
anos = int(input('Em quanto anos deseja pagar? '))
prest = valor/(anos * 12)
minimo = salario * 30 / 100
print('A Prestacao será de {:.2f} reais'.format(prest))
if prest <= minimo:
    print('o seu empréstimo de {:.2f} reais foi autorizado, com prestaçoes de {:.2f} reais mensais, no período de {:.2f} anos'.format(valor, prest, anos), end='')
else:
     print('Desculpe, o empréstimo de {:.2f} reais não pode ser efetuado pois a prestação de {:.2f} ultrapassa 30% de sua renda mensal.'.format(valor, prest), end='')