print('''  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/''')

print('Welcome to Treasure Island!\n')
print('How you doing?\n')
print('We gotta a treasure to find to rescue our teammates.\n')
print('Lets begin the Hunt! Hope you will be the rescuer. All the best for your journey Ahead!!!')
choice1=input('Welcome to the starting point. You\'re having  2 ways, choose any one.Take a "Left" or a "Right."\n').lower()
if choice1=="right":
    print('Congrats we have reached level 2! We can make this come on lets hurry up!')
    
    choice2= input('We have 2 choices to reach the treasure either you "swim" or you choose to "walk" to reach the next clue, Choose anyone.\n').lower()
    if choice2=='walk':
       print("woaahhoo!! We have made it to the next clue!")
      
       choice3= input('You are just 1 step away from the treasure. You have 2 boxes a "black Box" and a "small box" choose any 1 to find the keys for the treasure chest.\n').lower()
       if choice3=="black box":
          print("Congrats you found the key for the treasure chest!")
        
          choice4 = input('There are 2 treasure chests one in a "dig hole" and the other at the "sea shore".Which treasure chest will you choose to open.\n').lower()
          if choice4=="dig hole":
             print("You found the treasure. Congratulations You won!")
          elif choice4=="sea shore":
             print("It was a pirate trap. You lost.")
          else:
              print("You have entered an Invalid Input. You lost.")
          
       elif choice3=="small box":
          print("You lost the game. The small box had a poisonous snake in it that bit you very hard.")
       else:
           print("You have entered a wrong input. You lost.") 
    elif choice2=="swim":
      print("You lost the game. You were eaten by a Shoal of Piranas.")
    else:
        print("You have entered an invalid input. You lost the game.")
    
elif choice1=="left":
    print('You lost. You fell in a pit hole')
else:
    print("Invalid Input. You lost the game.")

