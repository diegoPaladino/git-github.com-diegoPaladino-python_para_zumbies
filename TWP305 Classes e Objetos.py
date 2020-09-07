#name of tutorial: TWP305 Classes e Objetos
#link of tutorial: https://www.youtube.com/watch?v=52ns4X7Ny6k


#exemplo de conversão necessária da entrada (que virá como string) de números: (exemple of necessary conversion of entries (that will come as string type) of numbers)

# n1 = input('N1: ')
# n2 = input('N2: ')
# print(n1 + n2)

#In the exemple above, the entries will came as string, resulting in the aswer: " 1213 " (assuming we put N1: 12 and N2:13, respectivaly)
#So, to solution, we declare like int or float:
# n1 = int(input('N1: '))
# n2 = int(input('N2: '))
# print(n1 + n2)    

#in float exemple:
# n1 = float(input('N1: '))
# n2 = float(input('N2: '))
# print(n1 + n2)

#lista de exercicios:
#bit.ly/PPZPythonExercicios
#tinyurl.com/PPZPythonExercicios

#_________________________________________________________________________________________________

#primeiro exercicio (o mesmo do exemplo do tutorial) | first exercise(the same of the tutorial)
# n1 = int(input('1º número:'))
# n2 = int(input('2º número:'))
# print(n1+n2)

#_________________________________________________________________________________________________

#segundo exercicio | second exercise
# print(f'Milímetros:{m*1000}')

#terceiro exercício | third exercise
# d = int(input('Dias:'))
# h = int(input('Horas:'))
# m = int(input('Minutos:'))
# s = int(input('Segundos:'))

# total = d*24*60*60 + h*60*60 + m*60 + s
# print(total)

#_________________________________________________________________________________________________
#quarto exercício | fourth execise
# s = float(input('Salário:'))
# p = float(input('Aumento%:'))
# aumento = s * p/100
# novo = s + aumento
# print(f'Aumento: R$ {aumento:.2f}')
# print(f'Novo salário: R$ {novo:.2f}')

#_________________________________________________________________________________________________
#quinto exercício | fifth execise
# m = float(input('Preço:'))
# p = float(input('Desconto%:'))
# desconto = m * p / 100
# novo = m - desconto
# print(f'Desconto: R${desconto:.2f}')
# print(f'Preço a pagar: {novo:.2f}')

#_________________________________________________________________________________________________
#sexto exercício | sixth execise
# d = float(input('Distância km:'))
# v = float(input('Vel. média km/h:'))
# t = d/v
# print(f'Tempo: {t:.1f}')

#_________________________________________________________________________________________________
#sétimo exercício | seventh execise
# c=float(input('Celsius: '))
# f = 9*c/5 + 32
# print(f'{f:.2f} Fahrenheit')

#_________________________________________________________________________________________________
#oitavo exercício | eighth execise
# f = float(input('Fahrenheit:'))
# c = (f-32)*5/9
# print(f'{c:.2f} Celsius')

#_________________________________________________________________________________________________
#nono exercício | nineth execise
# km = float(input('Km rodados: '))
# dias = int(input('Dias: '))
# preco = 60*dias + 0.15*km
# print(f'R$ {preco:.2f}')

#_________________________________________________________________________________________________
#décimo exercício | tenth execise
#fazendo uma regra de três
# cigarros = int(input('Cigarros dia: '))
# anos = int(input('Anos fumados: '))
# total_cigarros = anos * 365 * cigarros
# dias = total_cigarros / 144
# print(f'Voce perdeu {dias:.1f} dias')

#_________________________________________________________________________________________________
#décimo primeiro exercício | eleventh execise
print(len(str(2**1000000)))