print('===' *10)
print(' CREDIARIO MGS ')
print('===' *10)
salario=float(input('Entre com o valor do sálario:'))
bem=float(input('Entre com valor do bem:'))

#calcula o valor do bem que será comprado.
calcbem= (salario/100) * 30
if (bem <= calcbem):
    print('Crédito Liberado')
else:
    print('valor do bem superior a 30% do salário, Crédito Negado!!')