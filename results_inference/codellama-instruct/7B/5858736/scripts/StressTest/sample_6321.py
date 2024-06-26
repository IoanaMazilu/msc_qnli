chess_amateurs_premise = 4
chess_amateurs_hypothesis = 8

if chess_amateurs_hypothesis >= chess_amateurs_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
