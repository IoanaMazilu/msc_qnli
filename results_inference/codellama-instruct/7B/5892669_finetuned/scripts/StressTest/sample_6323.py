chess_amateurs_premise = 4
chess_amateurs_hypothesis = 4

# the hypothesis refers to the number of chess amateurs mentioned in the premise
if chess_amateurs_hypothesis >= chess_amateurs_premise:
    # check if the hypothesis value contradicts the exact number of chess amateurs in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
