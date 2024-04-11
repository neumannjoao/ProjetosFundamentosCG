############### FUNÇÕES ###############
def mediaUnisinos(grauA, grauB):
    media = (grauA + 2*grauB)/3.0
    return media
############### PROGRAMA PRINCIPAL ###############

grauA=float(input("digite sua média do Grau A:"))
grauB=float(input("digite sua média do Grau B:"))

grauFinal = mediaUnisinos(grauA, grauB)
print("Grau final é", grauFinal)