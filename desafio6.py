# Desafio ###########################################################################################################
# A empresa que você trabalha resolveu conceder um aumento salarial a todos funcionários, de acordo com a tabela abaixo:

# Salário	           Percentual de Reajuste
# 0 - 600.00           17%
# 600.01 - 900.00      13%
# 900.01 - 1500.00     12%
# 1500.01 - 2000.00    10%
# Acima de 2000.00     5%

# Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

# A entrada contém apenas um valor de ponto flutuante, que pode ser maior ou igual a zero, com duas casas decimais, conforme exemplos abaixo.

# Exemplo 1 #############################################################################################################
# Entrada	Saída 
# 1000      Novo salario: 1120,00 
#           Reajuste ganho: 120,00                                                                                     
#           Em percentual: 12 %

# Exemplo 2 #############################################################################################################
# Entrada	Saída 
# 2000      Novo salario: 2200,00                                                                                                   
#           Reajuste ganho: 200,00                                                                                                  
#           Em percentual: 10 %


# Resposta #########################################################################################################
salario = int(input()) 

if (salario <= 600.00  ):
  percentual = 0.17

elif ( salario <= 900.00 ):
  percentual = 0.13

elif ( salario <= 1500.00  ):
  percentual = 0.12

elif ( salario <= 2000.00  ):
  percentual = 0.10

else:
  percentual = 0.05

salario_novo = salario * (1 + percentual)

print(f"Novo salario: {salario_novo:.2f}")
print(f"Reajuste ganho: {salario_novo - salario:.2f}")
print(f"Em percentual: {percentual*100:.0f} %")