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

#primeiro exercicio (o mesmo do exemplo do tutorial) | first exercise(the same of the tutorial)
# n1 = int(input('1º número:'))
# n2 = int(input('2º número:'))
# print(n1+n2)

#_________________________________________________________________________________________________

#segundo exercicio | second exercise
# print(f'Milímetros:{m*1000}')

#terceiro exercício | third exercise
d = int(input('Dias:'))
h = int(input('Horas:'))
m = int(input('Minutos:'))
s = int(input('Segundos:'))

total = d*24*60*60 + h*60*60 + m*60 + s
print(total)

#_________________________________________________________________________________________________
#quarto exercício | fourth execise
s = float(input('Salário:'))
p = float(input('Aumento%:'))
aumento = s * p/100
novo = s + aumento
print(f'Aumento: R$ {aumento:.2f}')
print(f'Novo salário: R$ {novo:.2f}')
]