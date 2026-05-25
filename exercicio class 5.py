"""
Exercício: Formatador de Frases em Python

Objetivo:

Neste exercício, você será desafiado a criar uma aplicação Python
que ajuda os usuários a formatar frases de diversas maneiras. A aplicação
deve oferecer opções para converter toda a frase para maiúsculas ou minúsculas,
capitalizar a primeira letra, transformá-la em um título, contar
vogais e consoantes, e mais.

Requisitos:

    Crie uma classe chamada FormatadorDeFrase que será responsável por
    todas as operações de formatação.

    1. A classe deve possuir os seguintes métodos:

        para_maiusculas(): converte toda a frase para maiúsculas.
        para_minusculas(): converte toda a frase para minúsculas.
        capitalizar(): capitaliza a primeira letra da frase.
        formato_titulo(): converte a primeira letra de cada palavra da frase para maiúscula.
        contar_vogais(): conta e retorna o número de vogais na frase.
        contar_consoantes(): conta e retorna o número de consoantes na frase.
        contar_letra (): conta e retorna o número de ocorrências da letra  na frase.
        procurar_palavra(palavra): conta e retorna o número de ocorrências de uma palavra específica na frase.
        obter_frase(): retorna a frase atual.

    2. Implemente uma função menu que serve como interface do usuário. Essa
    função deve mostrar um menu com as opções de formatação e realizar a
    operação escolhida pelo usuário.

    3. O programa deve continuar rodando e mostrando o menu até que o usuário escolha sair.

Detalhes:

    O programa deve ser case-insensitive para contagem e pesquisa de palavras.
    Você pode assumir que o usuário entrará apenas com caracteres alfabéticos e espaços.

"""
class FormatadorDeFrase():

    def __init__(self,frase):
        self.frase = frase

    def para_maiusculas(self):

        self.frase = self.frase.upper()

        print(self.frase)

        return

    def para_minusculas(self):

        self.frase = self.frase.lower()

        print(self.frase)

        return

    def capitalizar(self):

        self.frase = self.frase.capitalize()

        print(self.frase)

        return

    def formato_titulo(self):

        self.frase = self.frase.title()

        print(self.frase)

        return

    def contar_vogais(self):

        vogais = [letra for letra in self.frase if letra in 'aeiouAEIOU']

        print(f'Essa frase possui {len(vogais)} vogais.')

        return len(vogais)

    def contar_consoantes(self):

        concoentes = [letra for letra in self.frase if letra.isalpha() and not letra in 'aeiouAEIOU']

        print(f'Essa frase possui {len(concoentes)} de consoantes.')

        return len(concoentes)

    def contar_letra(self,letra):

        quantidade = self.frase.lower().count(letra.lower())

        print(f'A {letra} aparece {quantidade} vezes na frase')

        return

    def contar_palavra(self,palavra):

        palavras = self.frase.lower().split()
        quantidade = palavras.count(palavra.lower())

        print(f'A {palavra} aparece {quantidade} vezes na frase')

    def obter_frase(self):

        print(f'{self.frase}')

entrada_frase = FormatadorDeFrase(input('digite uma frase: '))

while True:

    print('\n--menu--')
    print('1- converte todas as letras para maiusculas')
    print('2- converter para minusculas')
    print('3- converter para capitalizar')
    print('4- formatar toda letra inicial da frase para maiusculas')
    print('5- contar o numero de vogais')
    print('6- contar o numero de consoantes')
    print('7- contar o numero de ocorrencia de determinada letra')
    print('8- procurar palavra')
    print('9- obter frase atual')
    print('10- sair do programa')

    try:

      entrada = int(input('Escolha uma opção: '))

    except ValueError:

        print('entrad invalida')

        continue

    if entrada == 1:

        entrada_frase.para_maiusculas()

    elif entrada == 2:

        entrada_frase.para_minusculas()

    elif entrada == 3:

        entrada_frase.capitalizar()

    elif entrada == 4:

        entrada_frase.formato_titulo()

    elif entrada == 5:

        entrada_frase.contar_vogais()

    elif entrada == 6:

        entrada_frase.contar_consoantes()

    elif entrada == 7:

        escolha = input('Digite a letra que deseja verificar: ')

        entrada_frase.contar_letra(escolha)

    elif entrada == 8:

        escolha = input('Digite a palavra que deseja verificar: ')

        entrada_frase.contar_palavra(escolha)

    elif entrada == 9:

        entrada_frase.obter_frase()

    elif entrada == 10:

        print('finalizando....')
        print('Programa finalizado com sucesso!')

        break

    else:

        print('Entrada invalida')
        print('Escolha novamente')
