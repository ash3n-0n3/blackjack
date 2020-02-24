import random



dealer_hand = []
our_hand = []
cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]



dealer_hand.append(random.choice(cards))
dealer_hand.append(random.choice(cards))
our_hand.append(random.choice(cards))
our_hand.append(random.choice(cards))


print('dealer has {} and _ \n--------------------'.format(dealer_hand[0]))
print('our hand has {} and {}'.format(our_hand[0],our_hand[1]))

while sum(our_hand) < 21:
  respond = input('hit(h), stay(s), doubledown(d) \n')
  if respond == 'h':
      our_hand.append(random.choice(cards))
      print('You draw {}!'.format(our_hand[-1]))
      print('we are now = {}'.format(sum(our_hand)))
      
  elif respond == 's':
      break
      
if sum(dealer_hand) < sum(our_hand):
  while sum(dealer_hand) < 17:
      dealer_hand.append(random.choice(cards))

if sum(our_hand) > 21:
  print('Dealer has {}'.format(dealer_hand))
  print('You Lost!')
elif sum(our_hand) == 21:
  print('BlackJack! You Win!')
elif sum(dealer_hand) > 21:
  print('You Win!')
  print('Dealer has {}'.format(dealer_hand))
elif sum(our_hand) > sum(dealer_hand):
  print('You Win!')
elif sum(our_hand) == sum(dealer_hand):
  print('Draw!')
else:
  print('You Lost!')
  print('Dealer has {}'.format(dealer_hand))






