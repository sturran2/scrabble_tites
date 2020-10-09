letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
#zip files together to form a dictionary
letters_to_points={letter: point for letter,point in zip(letters, points)}
#add the blank tile
letters_to_points[" "]=0

#create function that return points that the word is worth.
def score_word(word):
  #make word point variable
  point_total=0
  for letter in range(0, len(word)):
    try:
      point_total+=letters_to_points[word[letter].upper()]
    except KeyError:
      point_total+=0
  return point_total

#test the function
#brownie_points=score_word("brownie")
#print(brownie_points)


#create a dicutionary that lists players to the list of words they have played. 

player_to_words={"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", 'BELLY', 'HUSKY'], "Prof Reader": ['ZAP', 'COMA', 'PERIOD']}

#Create empty dictionary
player_to_points={}



#define function play word that takes a player, and a word and add that word to the list of words they have played
def play_word(player, word):
  try:
    wordlist=player_to_words[player]
    wordlist.append(word)
    player_to_words[player]=wordlist
  except KeyError:
    print("player "+ player+ " does not exist")
play_word("Lei Con", "excuses")


#make a function for updating point totals with each new word.
def update_point_totals(player, word):
  play_word(player,word)
  for player, words in player_to_words.items():
    player_points=0
    for word in words:
      player_points+=score_word(word)
    player_to_points[player]=player_points
  print(player_to_words)
  print(player_to_points)

update_point_totals("Prof Reader", "Cosmic")

#print(player_to_points)
#print(letters_to_points)
