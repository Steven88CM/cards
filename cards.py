#flashcards
import random
import sys

vraagFile = open ("vragen.txt", "r")
antwFile = open ("antwoorden.txt", "r")

cards = vraagFile.readlines()
cardBack = antwFile.readlines()

print (cards)
print (cardBack)

inp = "yess"
while inp != "q":
  randomCard = random.choice(cards)
  index = cards.index(randomCard)
  backCArd = cardBack [index]
  print("")
  print(randomCard)
  inp = str(input())
  print("")
  print(backCArd)

sys.exit()

#numberOfCards = int(input("How many cards do you want? "))
#currentCardNumber = 0
#cards = list()
#while currentCardNumber < numberOfCards:
#    cards.append(str(input("For card " + str(currentCardNumber + 1) + ", what is the front?: ")))
#    currentCardNumber += 1
#print (cards)
#print ("")
#
#cardbacknum = 0
#cardBack = list()
#while cardbacknum < numberOfCards:
#    cardBack.append(str(input("For card " + str(cardbacknum + 1) + ", what is the back?: ")))
#    cardbacknum += 1
#print (cardBack)
#print ("")

#  print (randomCard) 
#  usrinput = str(input())
#  if usrinput + "\n" == backCArd:
#    print("juist"
#    print(backCArd)
#  else:
#    print ("fout")
#    print(backCArd)



