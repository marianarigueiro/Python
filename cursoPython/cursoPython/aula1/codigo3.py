# O código executa de cima para baixo.

faturamento = 1000 #Tipo: int -> Número inteiro
custo = 700

novas_vendas = 100
faturamento = faturamento + novas_vendas

imposto = faturamento * 0.1
lucro = faturamento - custo - imposto

margem_lucro = lucro / faturamento

print("Faturamento foi de " , faturamento)
print("O custo foi de " , custo)
print("O lucro foi de " , lucro)
print("A margem de lucro foi de " , round(margem_lucro, 1))

# Variáveis

mensagem = "O faturamento da loja foi de tanto..."
email = "emailqualquier@gmail.com"

teve_lucro   = True # Variavel tipo boolean

