import random

x = random.randint(0, 10)
erros = 0

while(erros < 3):
    
      print("##### Adivinhe o número ######")
      tentativa = int(input("Digite um número inteiro: "))
      print("#"*20, "\n")
      
      if tentativa == x:
            print("Você acertou!!!")
            break;
      else:
            erros = erros + 1
            if erros == 3:
                print("Você perdeu")
                break;
            print("Tente outra vez")
            
            if tentativa > x:
                print("Tente um número menor")
            else:
                print("Tente um número maior")
            print("#"*20, "\n")
print(f"tentativas: {erros}")         
    
