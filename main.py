número = int(input("Digite um número inteiro: "))
if número <= 0:
    print("Número inválido")
else:
    if número > 1:
        for i in range(2, número):
            if número % i == 0:
                print ("Não primo")
                break
        else:
            print("Primo")
                
    else:
        print("Não primo")
            
    


