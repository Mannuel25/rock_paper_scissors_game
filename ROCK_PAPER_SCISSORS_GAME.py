import random

def rockPaperScissorsGame():
	userScore = 0
	computerScore = 0
	playersScores = {'Computer':0,'Player 1':0}
	print('Welcome Player!')
	play_game = input('Do you want to play?(yes/no): ')	
	while True:
		n = random.randint(1,3)
		if n == 1:
			computer = 'rock'
		if n == 2:
			computer = 'paper'
		if n == 3:
			computer = 'scissors'
		if play_game.title() == 'Yes' or play_game.title() == 'YES':
			print('\nGreat!..let\'s get started player...')
			print('+ The winner earns a point after each round..Have fun player!!')
			user = input('Enter your choice(rock, paper, scissors): ')
			user = user.lower()
			if user == 'rock' or user == 'paper' or user == 'scissors':
				print('Computer selected {}'.format(computer))
				print('You selected {}'.format(user))
				if user == 'rock':
					if computer == 'paper':
						computerScore += 1
						playersScores['Computer'] = computerScore
						print('Computer wins!..paper wraps rock')
					elif computer == 'scissors':
						userScore += 1
						playersScores['player 1'] = userScore
						print('You win!..rock smashes scissors')
					elif computer == 'rock':
						print('No winner!!..play again to determine the winner')
					print('\nPlayers \t\t    Points')	
					print('-' * 34)
					print('{} \t\t    {}pts'.format('Player 1'.capitalize(), userScore))
					print('{} \t\t    {}pts'.format('Computer', computerScore))	
					play_game = input('\nDo you wanna play again?(yes/no): ')
				elif user == 'paper':
					if computer == 'rock':
						userScore += 1
						playersScores['player 1'] = userScore
						print('You win!..paper wraps rock')
					elif computer == 'scissors':
						computerScore += 1
						playersScores['Computer'] = computerScore
						print('Computer wins!..scissors cuts paper')
					elif computer == 'paper':
						print('No winner!!..play again to determine the winner')
					print('\nPlayers \t\t    Points')	
					print('-' * 34)
					print('{} \t\t    {}pts'.format('Player 1'.capitalize(), userScore))
					print('{} \t\t    {}pts'.format('Computer', computerScore))
					play_game = input('\nDo you wanna play again?(yes/no): ')
				elif user == 'scissors':
					if computer == 'paper':
						userScore += 1
						playersScores['player 1'] = userScore
						print('You win!..scissors cuts paper')
					elif computer == 'rock':
						computerScore += 1
						playersScores['Computer'] = computerScore
						print('Computer wins!..rock smashes scissors')
					elif computer == 'scissors':
						print('No winner!!..play again to determine the winner')
					print('\nPlayers \t\t    Points')	
					print('-' * 34)
					print('{} \t\t    {}pts'.format('Player 1'.capitalize(), userScore))
					print('{} \t\t    {}pts'.format('Computer', computerScore))	
					play_game = input('\nDo you wanna play again?(yes/no): ')
			else:
				print('Invalid choice!!')
				break
		else:
			break

		

rockPaperScissorsGame()
