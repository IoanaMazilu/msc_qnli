chess_amateurs_premise = 4
chess_amateurs_hypothesis = 4

# the hypothesis talks about the number of chess amateurs playing in the tournament, referenced also in the premise
if chess_amateurs_hypothesis >= chess_amateurs_premise:
    # check if the hypothesis value contradicts the exact number of 'chess_amateurs_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
