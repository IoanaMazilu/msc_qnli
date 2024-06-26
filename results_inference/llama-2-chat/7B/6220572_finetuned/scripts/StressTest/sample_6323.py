chess_amateurs_premise = 4
chess_amateurs_hypothesis = 4

# the hypothesis talks about the number of chess amateurs playing in the tournament, referenced also in the premise
if chess_amateurs_hypothesis <= chess_amateurs_premise:
    # check if the hypothesis value contradicts the number of chess amateurs in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of chess amateurs
    # any number of chess amateurs greater than 'chess_amateurs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
