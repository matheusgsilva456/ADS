nregimental=float(input('Entre com nota da regimental: \n'))
pRegimental=5

nparcial=float(input('Entre com nota da parcial: \n'))
pParcial=3

ntrabalho=float(input('Entre com nota do trabalho: \n'))
pTrabalho=2

# calcula média
media = (nregimental*pRegimental + nparcial*pParcial+ ntrabalho *pTrabalho) / (pRegimental+pParcial+pTrabalho)
if (media >= 6):
   msg="Aprovado"
   
elif (3<=media<6 ) :
    msg="Exame"

elif (media <3):
    msg="Reprovado"
print(msg)