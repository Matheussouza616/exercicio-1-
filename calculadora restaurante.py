prato churrasco = 30
prato refrigerante = 10
prato sobremesa = 20

quantidadeChurrasco = int (imput("quantidade de pratos de chrrasco: "))
quantidadeRefrigerante = int(imput("quantidade de refrigerantes: "))
quantidadeSobremesa = int(imput("quantidade de sobremesa: "))

subtotal = preçoChurrasco * quantidadeChurrasco
subtotal = preçoRefrigerante * quantidadeRefrigerante
subtotal = preçoSobremesa * quantidadeSobremesa

total = subtotalChurrasco + subtotalRefrigerante + subtotalSobremesa 
taxadeserviço = total * 0.1
totalComTaxa = total = taxadeserviço

pessoas = int(imput("quantas pessoas vão pagar a conta: "))
valorPorPessoa = totalComTaxa / pessoas 

print(f"R$ {total:.2f}")
