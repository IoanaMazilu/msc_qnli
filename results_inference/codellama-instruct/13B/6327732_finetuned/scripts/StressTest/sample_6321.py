chess_amateurs_premise = 4
chess_amateurs_hypothesis = 8

# the hypothesis talks about the number of chess amateurs playing in Villa's chess club tournament
if chess_amateurs_hypothesis <= chess_amateurs_premise:
    # check if the hypothesis value contradicts the number of chess amateurs in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of chess amateurs playing in Villa's chess club tournament
    # any number of chess amateurs less than 'chess_amateurs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)