#vetores dados
v1= [1, 5, 9, 2, 5]
v2= [7, 4, 13, 21, 6]
v3= [8, -3, 5, 7, 12]

M= [v1, v2, v3]

for linha in M:
    print(' '.join(map(str, linha)))
    