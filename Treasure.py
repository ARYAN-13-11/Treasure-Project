print('''
                             ,-.. _. ,. ,._
                                  .-'         .     '.
                                 /             .      /_./.
                                '                        '.
                               .                           '
                              '            =\ : , \         \
                             '            '` `   `  =        '
                             |,.        _\           ',       \
                             /   \    ."               ',.    /
                            || ,' `  ,                  ' \_.'
                            |\ -. / ,       `'":,      /
                          ,-= .   ,'       '_   `;.    |
                         /  /  -'            "'`    ,:,
                      _,/|,'    ,                   '
               ___,--' | |                    (    /
          _,-'`        . .      .            , '- _'          .-.
        ,'              \        .       `,'"`';/.          ,'   )
      ,`                 .'       :     /  ';\\   '.     ,'    .'
    ,'                   |.\       ';.'.,. .;.\\  ,..:_'_    .
   /  .                    '.       .'';_:;'`  '_(        ' '-.
   |   .                     '.'.,-'   ,       (    '" - ._    )
  / .   `                      '.             _,'-._        ` (
 /    .                    _ |   '      .' '.    ' .  _       )
                              (:)          '      '        '   '
''')
print("Welcome to No Man's Land.")
print("Your mission is to find a man.\n")
adventure = input("Are you ready for an adventure? \n  "
                  "Type \"Y\" if yes or \"N\" if No\n").lower()
if adventure == "y":
    volcano = input("You've come to the volcano. You have to jump in it or run from it. \n"
          " Type \"jump\" to jump in the volcano. "
                    "Type \"run\" to run from the volcano.\n").lower()
    if volcano == "jump":
        treasure = input("You Have found the treasure!!! But it is locked with a passcode."
                         " \nYou have only 1 Try.\n There are 3 combinations you can try."
                         " \"00\", \"69\" or \"7\" \n")
        if treasure == "00":
            print("Oops Incorrect Passcode!!! You die from explosion.")
        elif treasure == "69":
            print("Congrats Correct Passcode!!! You are now rich in your dreams. ")
        elif treasure == "7":
            print("Oops Incorrect Passcode!!! You die from explosion.")
        else:
            print("How can you not even put the combination properly!!! You deserve to die.")
    else:
        print("You never run from your problems. You are dead.")
else:
    print("There is no space here for cowards. You are dead.")
