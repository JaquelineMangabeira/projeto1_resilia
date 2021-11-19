print('''Bem vindo ao Resgate Silvestre! O jogo te leva em uma aventura pela Mata Atlântica para viver os desafios de proteger nossos animais em extinção e conhecer mais a biodiversidade do Brasil. 

Todos os pontos do jogo serão revertidos para instituições que realizam trabalho de resgate, denúncia e proteção animal.

A sua missão é salvar  o Mico-Leão Dourado, a Onça-pintada e a Arara Azul dos perigos dos caçadores, traficantes e comércio ilegal.

Você pode escolher entre: Veterinário, Biólogo e Protetor da Florestas.''')

#escolha de personagens

def escolha_seu_personagem():
	is_valid = True
	while(is_valid):
		personagem = input('Escolha o seu personagem: 1 - Biólogo, 2 - Veterinário, 3 - Protetor das Florestas')
		if personagem == '1':
			nome_personagem = 'Biólogo'
			is_valid = False
			return nome_personagem

		elif personagem == '2':
			nome_personagem = 'Veterinário'
			is_valid = False
			return nome_personagem
			
		elif personagem == '3':
			nome_personagem = 'Protetor das Florestas'
			is_valid = False
			return nome_personagem
		else:
			print('Personagem não encontrado! Digite um número válido.')


print('O Biólogo Cauã Mangabeira atua dentro e na borda das florestas impedindo o comércio ilegal de animais e fazendo o cuidado deles para reintrodução no habitat natural. O seu maior objetivo é o resgate animal. Com a sua corda mágica ele consegue prender vendedores e compradores ilegais.Nesta fase o seu objetivo é curar o maior número de animais e derrotar caçadores. Ao finalizar a fase você acumulará pontos para o próximo objetivo.')

	


def biologo_fase1(pontos):
	while True:
		caminho = input('Escolha o seu caminho: 1 - Feira de Vendas, 2 - Trabalho de Campo, 3 - Floresta')
		if caminho == '3':
			print('Game Over')
			pontos = -1
			return pontos
		elif caminho == '2':
			print('5 pontos')
			pontos = pontos + 5
			return pontos
		elif caminho == '1':
			print('10 pontos')
			pontos = pontos + 10
			return pontos
		else: 
			print("caminho inválido, tente novamente")
def biologo_fase2(pontos):
	while True:
		caminho = input('Escolha o seu caminho: 1 - Feira de Vendas, 2 - Trabalho de Campo, 3 - Floresta')
		if caminho == '3':
			print('Game Over')
			pontos = -1
			return pontos
		elif caminho == '2':
			print('5 pontos')
			pontos = pontos + 5
			return pontos
		elif caminho == '1':
			print('10 pontos')
			pontos = pontos + 10
			return pontos
		else: 
			print("caminho inválido, tente novamente")
def biologo_fase3(pontos):
	while True:
		caminho = input('Escolha o seu caminho: 1 - Feira de Vendas, 2 - Trabalho de Campo, 3 - Floresta')
		if caminho == '3':
			print('Game Over')
			pontos = -1
			return pontos
		elif caminho == '2':
			print('5 pontos')
			pontos = pontos + 5
			return pontos
		elif caminho == '1':
			print('10 pontos')
			pontos = pontos + 10
			return pontos
		else: 
			print("caminho inválido, tente novamente")



def resultado(pontuacao_final):
	pontos=pontuacao_final
	print(f'O resultado final foi {pontos}!')


#Personagem Veterinário	

print('''O Veterinário Rafael Caapora explora as florestas para encontrar animais feridos, curá-los e ajudá-los. A missão dele é proteger os animais e curá-los com seus poderes mágicos. A arma é a Seringa Sonífero e seu maior vilão é o Caçador Corvo.''')


def veterinario_fase1(pontos):
	while True:
		caminho = input('Escolha o seu caminho: 1 - Feira de Vendas, 2 - Trabalho de Campo, 3 - Floresta')
		if caminho == '3':
			print('Game Over')
			pontos = '-1'
			return pontos
		elif caminho == '2':
			print('5 pontos')
			pontos = pontos + 5
			return pontos
		elif caminho == '1':
			print('10 pontos')
			pontos = pontos + 10
			return pontos
		else: 
			print("caminho inválido, tente novamente")
def veterinario_fase2(pontos):
	while True:
		caminho = input('Escolha o seu caminho: 1 - Feira de Vendas, 2 - Trabalho de Campo, 3 - Floresta')
		if caminho == '3':
			print('Game Over')
			pontos = -1
			return pontos
		elif caminho == '2':
			print('5 pontos')
			pontos = pontos + 5
			return pontos
		elif caminho == '1':
			print('10 pontos')
			pontos = pontos + 10
			return pontos
		else: 
			print("caminho inválido, tente novamente")
def veterinario_fase3(pontos):
	while True:
		caminho = input('Escolha o seu caminho: 1 - Feira de Vendas, 2 - Trabalho de Campo, 3 - Floresta')
		if caminho == '3':
			print('Game Over')
			pontos = -1
			return pontos
		elif caminho == '2':
			print('5 pontos')
			pontos = pontos + 5
			return pontos
		elif caminho == '1':
			print('10 pontos')
			pontos = pontos + 10
			return pontos
		else: 
			print("caminho inválido, tente novamente")

#Personagem Protetor Florestal

print('''Extremamente conectada com a Floresta, a protetora florestal Tainá Ozibel  fica nas florestas demarcando territórios protegidos, desatando armadilhas, prendendo caçadores e ajudando os animais. A sua missão é proteger a floresta dos roubos do Traficante El Diablo. Com seu walk-talk radioativo, Tainá consegue cumprir sua missão.
''')
	


def protetor_florestal_fase1(pontos):
	while True:
		caminho = input('Escolha o seu caminho: 1 - Feira de Vendas, 2 - Trabalho de Campo, 3 - Floresta')
		if caminho == '3':
			print('Game Over')
			pontos = -1
			return pontos
		elif caminho == '2':
			print('5 pontos')
			pontos = pontos + 5
			return pontos
		elif caminho == '1':
			print('10 pontos')
			pontos = pontos + 10
			return pontos
		else: 
			print("caminho inválido, tente novamente")
def protetor_florestal_fase2(pontos):
	while True:
		caminho = input('Escolha o seu caminho: 1 - Feira de Vendas, 2 - Trabalho de Campo, 3 - Floresta')
		if caminho == '3':
			print('Game Over')
			pontos = -1
			return pontos
		elif caminho == '2':
			print('5 pontos')
			pontos = pontos + 5
			return pontos
		elif caminho == '1':
			print('10 pontos')
			pontos = pontos + 10
			return pontos
		else: 
			print("caminho inválido, tente novamente")
def protetor_florestal_fase3(pontos):
	while True:
		caminho = input('Escolha o seu caminho: 1 - Feira de Vendas, 2 - Trabalho de Campo, 3 - Floresta')
		if caminho == '3':
			print('Game Over')
			pontos = -1
			return pontos
		elif caminho == '2':
			print('5 pontos')
			pontos = pontos + 5
			return pontos
		elif caminho == '1':
			print('10 pontos')
			pontos = pontos + 10
			return pontos
		else: 
			print("caminho inválido, tente novamente")

def resultado(pontuacao_final):
	pontos=pontuacao_final
	print(f'O resultado final foi {pontos}!')



nome_personagem = escolha_seu_personagem()
if nome_personagem == 'Biólogo':
	biologo_fase1()
	biologo_fase2()
	biologo_fase3()


	
elif nome_personagem == 'Veterinário':
	veterinario_fase1()
	veterinario_fase2()
	veterinario_fase3()

else:
	protetor_florestal_fase1()
	protetor_florestal_fase2()
	protetor_florestal_fase3()