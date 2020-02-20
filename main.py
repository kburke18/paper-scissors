import paper_scissors;

print("""
=============
This is a game of Paper-Scissors. There are 5 rounds. Each player is allowed to use their Scissors two (2) times.
Scissors beat Paper. Matching calls make a draw.
=============

""");
playing = True;
correct_input = False;

while (playing) :
    correct_input = False;
    paper_scissors.play();
    while (not(correct_input)) :
        play_again = input("Play again? Y/N \n").lower();
        if ("n" in play_again) :
            playing = False;
            correct_input = True;
        elif("y" in play_again) :
            correct_input = True;
            print("Restarting game....");

print ("Thanks for playing!");
