# Escreva um algoritmo que solicite ao seu usuário a média de um aluno e o percentual de frequência e mostre a sua situação,conforme a tabela abaixo.

media  = float(input("Digite a média do aluno:"))
frequencia = float(input("Digite a frequencia do aluno: "))

if frequencia < 75:
    print("Reprovado por falta") 
elif media < 6:
    print("Reprovado por nota")
else:
    print("Aprovado = ferias")        