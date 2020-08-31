#resposta
#edition_mode(5:48 - https://www.youtube.com/watch?v=qHx8SRYqW2E&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc&index=4)

# _______________________________________________________
# resposta = 42
# print('Resposta para tudo é: ',resposta)
# print(f'tudo tem {resposta} como sulução')
# preço = 9.666666
# print(f'preço é R$ {preço:.2f}')
# _______________________________________________________
#operadores relacionais (relational operators)

# a = 42
# b = 13
# # print(a > b)
# # print(type(True))

# _________________________________________________________________________________________________________
#NAME: TWP040 Operadores Relacionais e lógicos
#LINK: https://www.youtube.com/watch?v=pDi5VtF9TfA&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc&index=5

# _______________________________________________________
#testes lógicos(logic tests)
#equal
# a1 = a == 42
# b1 = b == 42
# print('the aswer to "a1" is: ',a1)
# print('the aswer to "b1" is: ',b1)

# _______________________________________________________
#different comparator
# a2 = a != 42
# b2 = b != 42
# print('the aswer to "a2" is: ',a2)
# print('the aswer to "b2" is: ',b2)

# _______________________________________________________
#or comparator
# c1 = a == 42 or b == 42
# print('the aswer to "c1" is: ',c1)

# _______________________________________________________
#and comparator
# nota = 7
# faltas = 21

# print('Aprovação:',nota >= 6 and faltas <=20)

# _________________________________________________________________________________________________________
#NAME: TWP050 Entendendo conceitos sobre linguagem dinâmica e tipagem forte
# LINK: https://www.youtube.com/watch?v=Az0ri1W2Ygc&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc&index=6

a = 42
a = 'abacate'
a = 3.14
# 42+'abacate' #nessa forma haverá erro, portanto nessecita-se explicitar
print(str(42) + ' abacates')

a = 3
b = 'abacate'

#atribuição multipla (multiple assignment)
#contrário de diversas outras linguagens, o python permite a atribuição multipla de variaveis:

a,b = b,a
print(a)

a,b,c=1,2,3
print(a,b,c)

d,m,a='30/08/2020'.split('/')
print(d,m,a)

