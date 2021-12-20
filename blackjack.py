import random
play_count = 0
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer = []
player = []
random_cards = []
game_ended = False
game_logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_/
      |  \/ K|                            _/ |                
      `------'                            |__/
"""
# print(game_logo)

def serveCards():
    print('called')
    # Get four random cards from the deck and serve them to them
    # equally among two players.
    for i in range(0, 4):
        random_card_index1 = random.randint(0, len(cards) - 1)
        if len(dealer) == 0 or len(dealer) == 1:
            dealer.append(cards[random_card_index1])
        else:
            player.append(cards[random_card_index1])
    print(game_logo)
    print(cardsSelected())

def cardsSelected():
    return (
        f'Your cards: {player}, current score: {player[0] + player[1]}\n'
        f'Computers first card: {dealer[0]}'
    )


if play_count == 0:
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if str(start_game).lower() == 'y':
        serveCards()