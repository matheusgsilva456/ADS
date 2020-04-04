nregimental=float(input('Entre com nota da regimental: \n'))
pRegimental=5

nparcial=float(input('Entre com nota da parcial: \n'))
pParcial=3

ntrabalho=float(input('Entre com nota do trabalho: \n'))
pTrabalho=2

# calcula média
media = (nregimental*pRegimental + nparcial*pParcial+ ntrabalho *pTrabalho) / (pRegimental+pParcial+pTrabalho)

if (media >= 6):
   msg="Aluno Aprovado"
   recomendacao="Parabéns"
else:
    msg="Aluno Reprovado"
    recomendacao="Estude Mais"
print(msg)
print(recomendacao)
