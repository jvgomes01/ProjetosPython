#leitura de numeros

#Interação com o usuario(dados serã o inseridos)
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo numero: '))
num3 = float(input('Digite o terceiro número'))
valores = [num1, num2, num3]

#validação de igualdade

#caso os numeros sejam diferentes, o programa ira responder com uma lista em ordem crescente
if num1 != num2 and num3:
    if num2 != num1 and num3:
        if num3 != num1 and num2:
            print(sorted(valores))
#caso tenha algum número repetido, o programa irá exibir a mensagem de atenção
if num1 == num2 and num3:
    if num2 == num1 and num3:
        if num3 == num1 and num2:
            print('Atenção! Por favor, não repita os números!')






















