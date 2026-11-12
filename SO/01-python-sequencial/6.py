# Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos.
# Variaveis
x: float = 0.0
y: float = 0.0

# Inicio
x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

temp = x
x = y
y = temp
print("O valor de x após a troca é: ", x)
print("O valor de y após a troca é: ", y)
# Fim