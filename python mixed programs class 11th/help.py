# help menu to learn basic python features and programs.
(input())
print ("hi, please enter your name.")
NAME =(input())
print ("welcome",NAME,",how can we help you?")
print ('''you can ask things like:-
        * how can i turn on dark mode?
        * how can i increase the font size?
        * how to add two numbers?
        * how to multiply two numbers?
        * how to make a basic calculater?
        * how to calculate leap year?
        * can you play a game?''')
P ="how can i turn on dark mode?"
Q ="how can i increase the font size?"
R ="how to add two numbers?"
S ="how to multiply two numbers?"
T ="how to make a basic calculater?"
U ="how to calculate leap year?"
V ="can you play a game?"
A =(input())
if A==P:
    print ('''    1. Go to options dropbox on the top left corner of the screen.
    2. click on configure idle.
    3. click on highlights.
    4. select the desired view mode from there.''')
elif A==Q:
    print ('''    1. Go to options dropbox on the top left corner of the screen.
    2. click on configure idle.
    3. select the desired size from there.''')
elif A==R:
    print ('''   code:-
    A =int(input("enter number"))
    B =int(input("enter number"))
    print (A+B)''')
elif A==S:
    print ('''   code:-
         A =int(input("enter number"))
    B =int(input("enter number"))
    print (A*B)''')
elif A==T:
    print ('''     code:-
            A=float(input("enter first number: "))
            B=float(input("enter second number: "))
            C=input("enter operator(+,-,*,/,//,%): ")
            if C=='+':
                print(A+B)
            elif C=='-':
                print(A-B)
            elif C=='*':
                print(A*B)
            elif C=='/':
                print(A/B)
            elif C=='//':
                print(A//B)
            elif C=='%':
                print(A%B)
            else:
                print("invalid operator.")''')
elif A==U:
    print ('''      code:-
          #leap year
        A=int(input("enter year: "))
        if A%100==0 and A%400==0:
            print(A,"is a leap year.")
        elif A%100!=0 and A%4==0:
            print(A,"is a leap year.")
        else:
            print(A,"is not a leap year.")''')
if A==V:
    print("ok lets play a game.")
    print('''the game is called: guess the number.
    how to play: player1 has to think of a number and player2 has to guess the number.
        we can take turns for guessing the number.''')
    import guess_the_number_game
print ("         ")
print ("there you go",NAME)
