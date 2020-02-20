import random;

def play() :
    game_finished = False;
    game_rounds = 1;

    player_scissors = 2;
    player_value = False;
    player_score = 0;

    opponent_scissors = 2;
    opponent_value = False;
    opponent_score = 0;

    # cannot cast non-strings into string implicity. Must use format where each {}
    # is a variable
    txt_input = """Round {}:
    Score: {} vs {}

    Paper or Scissors? Scissors remaing: {}
    """;

    while (not(game_finished) and game_rounds <= 5) :

        # The player input stage
        player_choice = input (txt_input.format(game_rounds, player_score, opponent_score, player_scissors));
        player_choice.lower().strip();
        correct_input = False;
        while (not(correct_input)) :
            if ("scissors" in player_choice and player_scissors > 0) :
                player_value = True;
                player_scissors -= 1;
                correct_input = True;
            elif ("paper" in player_choice) :
                player_value = False;
                correct_input = True;
            else :
                print("Incorrect input. Please choose paper or scissors.")
                player_choice = input(txt_input.format(game_rounds, player_score, opponent_score, player_scissors));

        # Easy opponnent input stage
        if (opponent_scissors > 0) :
            opponent_choice = random.randint(0, 1);
            if (opponent_choice != 0) :
                opponent_value = True;
                opponent_scissors -= 1;
                print("Opponent chose Scissors.");
            else :
                opponent_value = False;
                print("Opponent chose Paper.");
        else :
            opponent_value = False;
            print("Opponent chose Paper.");

        # End of round stage
        if (player_value == opponent_value) :
            print("DRAW");
        elif(player_value == False and opponent_value == True) :
            print("Winner : Opponent");
            opponent_score += 1;
        else :
            print ("Winner : Player");
            player_score += 1;
        game_rounds += 1;

        # End game stage
        if (game_rounds > 5) :
            if (player_score == opponent_score) :
                print("GAME OVER. Game ends in DRAW. Try again...")
            elif (player_score > opponent_score) :
                print("GAME OVER. Winner is the Player! Congratulations!")
            else :
                print("GAME OVER. Winner is Opponent. Try again...")
            game_finished = True;
