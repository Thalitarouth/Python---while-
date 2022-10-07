
"""
x = 1
while x<=5:
    print(x,"\n")
    x= x + 1
    
 --------------------------------------------------------
    
fim_contagem = int(input("digite valor do contador ="))
x = 1
while x<= fim_contagem:
    print(x,"\n")
    x= x + 1
    
 ---------------------------------------------------------    

limite = int(input("entrar com o valor numérico limite"))
contador = 0
while contador <= limite:
    if contador % 2 == 0:
        print (contador, "\n")
    contador = contador + 1    
  --------------------------------------------------------
limite = int(input("entrar com o valor numérico limite"))
contador = 0
while contador <= limite:
    if contador % 2 == 1:
        print (contador, "\n")
    contador = contador + 1       
----------------------------------------------------------

numero = int( input("entrar com o valor numerico da tabuada"))
n = 1 
while n <= 10:
    print(numero,"\tx","\t",n,"\t",numero*n,"\n")
    n=n+1
    


comando = "continuar"
n=0
while comando != "parar": #!= ->diferente
     comando = input("entrar com o comando de continuar ou parar: \t")
     n=n+1
     print(n,"\t",comando)
     



senha = "gustavo"
n=1
while n<=3:
    entrada_usuario = input("Digite a senha\t")
    if entrada_usuario == senha:
        print("senha correta")
        break # break -> sai do laço
    else:
        n = n + 1
        print("senha errada")
        
        
  """      
b = int(input("quantos números irá somar?"))
n = 1
soma = 0 
while n<= b:
    a = int(input("entrar com valor do numero a somar: "))
    soma = soma + a
    n = n + 1 
print("valor da soma = ", soma) 

   
       
        
        
        
        
        
        
        
        
        
        
        

    