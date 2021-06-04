import random

hiragana_dict = {"a": u"\u3042", "i": u"\u3044", "u": u"\u3046", "e": u"\u3048", "o": u"\u304A",
"ka": u"\u304B", "ki": u"\u304D", "ku": u"\u304F", "ke": u"\u3051", "ko": u"\u3053",
"sa": u"\u3055", "shi": u"\u3057", "su": u"\u3059", "se": u"\u305B", "so": u"\u305D",
"ta": u"\u305F", "chi": u"\u3061", "tsu": u"\u3064", "te": u"\u3066", "to": u"\u3068",
"na": u"\u306A", "ni": u"\u306B", "nu": u"\u306C", "ne": u"\u306D", "no": u"\u306E",
"ha": u"\u306F", "hi": u"\u3072", "fu": u"\u3075", "he": u"\u3078", "ho": u"\u307B",
"ma": u"\u307E", "mi": u"\u307F", "mu": u"\u3080", "me": u"\u3081", "mo": u"\u3082",
"ya": u"\u3084", "yu": u"\u3086", "yo": u"\u3088",
"ra": u"\u3089", "ri": u"\u308A", "ru": u"\u308B", "re": u"\u308C", "ro": u"\u308D",
"wa": u"\u308F", "wo": u"\u3092", "n": u"\u3093"}

katakana_dict = {"a": u"\u30A2", "i": u"\u30A4", "u": u"\u30A6", "e": u"\u30A8", "o": u"\u30AA",
"ka": u"\u30AB", "ki": u"\u30AD", "ku": u"\u30AF", "ke": u"\u30B1", "ko": u"\u30B3",
"sa": u"\u30B5", "shi": u"\u30B7", "su": u"\u30B9", "se": u"\u30BB", "so": u"\u30BD",
"ta": u"\u30BF", "chi": u"\u30C1", "tsu": u"\u30C4", "te": u"\u30C6", "to": u"\u30C8",
"na": u"\u30CA", "ni": u"\u30CB", "nu": u"\u30CC", "ne": u"\u30CD", "no": u"\u30CE",
"ha": u"\u30CF", "hi": u"\u30D2", "fu": u"\u30D5", "he": u"\u30D8", "ho": u"\u30DB",
"ma": u"\u30DE", "mi": u"\u30DF", "mu": u"\u30D0", "me": u"\u30D1", "mo": u"\u30D2",
"ya": u"\u30E4", "yu": u"\u30E6", "yo": u"\u30E8",
"ra": u"\u30E9", "ri": u"\u30EA", "ru": u"\u30EB", "re": u"\u30EC", "ro": u"\u30ED",
"wa": u"\u30EF", "wo": u"\u30F2", "n": u"\u30F3"}

#to add special characters

def hiragana_fun():
    score = 0
    for q in range(10):
        print("Question # " + str(q+1))

        romh = random.choice(list(hiragana_dict.keys()))
        kanah = hiragana_dict[romh]
        answer = input("Enter a romaji for " + kanah + ": ")
        if answer.lower() == romh:
            print("Correct!")
            score += 2
        else:
            print("Wrong! Correct answer is " + romh + "!")
            score -=1
        print("Your score so far: " + str(score) + ".\n")
        if score < 0:
            print("You have to do better! Your score is a negative number now!")
    print("Total score: " + str(score) + " out of 20.\n")

def katakana_fun():
    score = 0
    for q in range(10):
        print("Question # " + str(q+1))

        romk = random.choice(list(katakana_dict.keys()))
        kanak = katakana_dict[romk]
        answer = input("Enter a romaji for " + kanak + ": ")
        if answer.lower() == romk:
            print("Correct!")
            score += 2
        else:
            print("Wrong! Correct answer is " + romk + "!")
            score -=1
        print("Your score so far: " + str(score) + ".\n")
        if score < 0:
            print("You have to do better! Your score is a negative number now!")
    print("Total score: " + str(score) + " out of 20.\n")

def restart():
    again = input("Would you like to play again? Y/N ")
    if again.lower() == "y":
        which_game()
        restart()
    else:
        print("Thanks for playing!")

def which_game():
    which = input("Which writing system would you like to practice? Hiragana/Katakana ")
    if which.lower() == "hiragana":
        hiragana_fun()
        restart()
    elif which.lower() == "katakana":
        katakana_fun()
        restart()
    else:
        print("Wrong input. Please choose again.")
        which_game()

which_game()