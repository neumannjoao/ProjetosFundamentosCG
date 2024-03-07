# smartphones
smartphones = float(input('insira o número de smartphones vendidos:'))

#tablets
tablets = float(input('insira o número de tablets vendidos:'))

#cálculo:
calcsmart = (smartphones * 1000)
calctab = (tablets * 1500)


print('valor total de smartphones vendidos', calcsmart)
print('valor total de tablets vendidos', calctab)


print('valor total vendido', calcsmart + calctab)