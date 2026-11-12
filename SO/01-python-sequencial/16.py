# Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes. Calcule o salário que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário Bruto – desconto). A cada dependente será acrescido R$ 100 no Salário Líquido. Exiba o salário a receber.
# Variaveis
horasTrabalhadas: float = 0.0
valorPorHora: float = 0.0
percentualDesconto: float = 0.0
numeroDependentes: int = 0
salarioBruto: float = 0.0
salarioLiquido: float = 0.0

# Inicio
horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valorPorHora = float(input("Digite o valor por hora: "))
percentualDesconto = float(input("Digite o percentual de desconto: "))
numeroDependentes = int(input("Digite o número de dependentes: "))
salarioBruto = horasTrabalhadas * valorPorHora
desconto = salarioBruto * (percentualDesconto / 100)
salarioLiquido = salarioBruto - desconto + (numeroDependentes * 100)
print("O salário a receber é: ", salarioLiquido)
# Fim