print('======== DESAFIO 04 ==========')

n = input('Digite algo: ')
print('O tipo primitivo desse valor e ', type(n)) #Diz o tipo da variável
print('É alfa-númerico?', n.isnumeric()) #informa se a variável é numerica
print('Está em maiúsculo? {}'.format(n.isupper())) #informa se a variável está em maiúsculo
print('É somento espaço?', n.isspace()) #informa se a variável é espaço
print('É alfabetico?', n.alpha()) #informa se é alfabetico 
