
import sys


print("Ola, seja bem-vindo(a) ao Cakes mania" )
print("======================================")
print("Menu bolo, a seguir selecione o sabor do bolo")
             
print("""
    Escolha o sabor do seu bolo:
    
    [1]- Fatia de Bolo brigaderiro = 15.80
    [2]- Fatia de Bolo ninho = 15.80
    [3]- Fatia de Bolo Chocolate = 14.90
    [4]- Fatia de Bolo frutas vermelhas = 14.90
    [5]- Fatia de Bolo Red velvet = 18.90
    [6]- Fatia de Bolo Devil's food cake = 18.90
        """)
escolha = str(input(" ")).lower().strip()
produto1 = ["Fatia de bolo brigaderiro"]
produto2 = ["Fatia de bolo de ninho"]
produto3 = ["Fatia de bolo de Chocolate"]
produto4 = ["Fatia de bolo de frutas vermelhas"]
prod5 =["Fatia de Bolo Red velvet"]
prod6 =["Fatia de Bolo Devil's food cake"]

if  escolha == "1":
    for item in produto1:
     print(item)
     
elif  escolha == "2":
    for item in produto2:
     print(item)
     
elif  escolha == "3":
    for item in produto3:
     print(item)    
     
elif  escolha == "4":
    for item in produto4:
     print(item)   
     
elif  escolha == "5":
    for item in prod5:
     print(item)
     
elif  escolha == "6":
    for item in prod6:
     print(item)
     
print("")   
print("Ok, confirmando...")
print("")
print ("Otima escolha," + item)
print("")
print("Gostaria de adicionar uma bebida ao seu pedido?")
print("""
    1- Sim
    2- Não
        """)
AlgoMais=str(input("")).lower().strip()
produto9 = ["Sim"]
produto10 = ["Não"]

if  AlgoMais == "1":
    for item1 in produto9:
     print(item1)   

elif AlgoMais == "2":
    print("OK, então vamos finalizar seu pedido...")
    print("")
    print("A seguir nos informe seu endereço para proseguirmos com sua entrega ;)\n")
    endereco= input("Informe seu endereço: \n")
    print("")
    Cep = input("Informe seu CEP: APENAS NUMEROS \n")
    print("")
    Bairro = input("Informe seu bairro: \n")
    print("")
    nome= input ("Informe seu nome: \n")
    print("")
    print ("Registrando endereço... \n") 
    print("Endereço " + endereco + "," " CEP " + Cep + " no bairro " + Bairro)
    print("")
    print("Confirmando informações, Seu pedido é " + item + ","  +" no endereço "
      + endereco +"", " CEP " + Cep + " no bairro " + Bairro)
    print("")
    print("Tempo estimado de entrega é de aproximadamente 30 min.")
    print("")
    print("Agradecemos a preferencia. Tenha um otimo dia " + nome)
    print("============================================") 
    sys.exit()
    
 
print("")
print(" bebida: ")    
     
print("""
    Escolha sua bebida:
    [1]- Coca cola = 7.00
    [2]- Suco de uva = 5.00
    [3]- Fanta laranja 7.00
    [4]- Agua = 4.80
        """)


produto9 = str(input("")).lower().strip()
produto5 = ["Coca cola"]
produto6 = ["Suco de uva"]
produto7 = ["Fanta laranja"]
produto8 = ["Agua"]     
     
if  produto9 == "1":
    for item1 in produto5:
     print(item1)
     
elif produto9 == "2":
    for item1 in produto6:
     print(item1)
     
elif  produto9 == "3":
    for item1 in produto7:
     print(item1)    
     
elif  produto9 == "4":
    for item1 in produto8:
     print(item1) 
    
print ("Confirmando Bebida....")
print("")
print("Ok, bebida confirmada " + item1)
print("...")
print("Confirmando pedido," + item + " e " + item1)
print("")
print("A seguir nos informe seu endereço para proseguirmos com sua entrega ;)\n")
endereco= input("Informe seu endereço: \n")
print("")
Cep = input("Informe seu CEP:APENAS NUMEROS \n")
print("")
Bairro = input("Informe seu bairro: \n")
print("")
nome= input ("Informe seu nome: \n")
print("") 
print ("Registrando endereço... \n")
print ("Endereço: " + endereco + " "," " " CEP " + Cep + " no bairro " + Bairro)
print("")
print("Confirmando informações, Seu pedido é um " + item + "," + item1 +" no endereço "
      + endereco + ","" CEP " + Cep + " no bairro " + Bairro)

print("")
print("Tempo estimado de entrega é de aproximadamente 30 min.")
print("")
print("Agradecemos a preferencia. Tenha um otimo dia " + nome)
print("===================================================")

     









    


