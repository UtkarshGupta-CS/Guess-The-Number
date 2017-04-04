import random

def guess():
   cond = True
   while (cond):
      random_num = random.randrange(0,100)
      ask = int(raw_input("Guess the no. between 0-99: "))

      if ask > random_num:
         print "The no. is too high!"
         cond = True

      elif ask < random_num:
         print "the no. is too low! "

      else:
         print "You guessed correct Yoohoo!"
         cond = False

guess()