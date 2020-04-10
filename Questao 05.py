n1 = int(input("Digite o primeiro valor: \n"))
n2 = int(input("Digite o segundo valor: \n"))
sinal = input("Digite o sinal operação: \n")

if sinal == "+":
    n3 = n1 + n2
    print ("Resultado: " + str(n3))
elif sinal == "-":
    n3 = n1 - n2
    print("Resultado: " + str(n3))
elif sinal == "*":
    n3 = n1*n2
    print("Resultado: " + str(n3))
elif sinal == "/":
    n3 = n1/n2
    print("Resultado: " + str(n3))
