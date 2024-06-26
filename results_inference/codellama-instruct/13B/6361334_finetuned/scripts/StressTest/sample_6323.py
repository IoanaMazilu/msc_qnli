chess_amateurs_premise = 4
chess_amateurs_hypothesis = 4

# the hypothesis refers to the number of chess amateurs playing in Villa's chess club tournament
if chess_amateurs_hypothesis <= chess_amateurs_premise:
    # check if the estimate of 'chess_amateurs_hypothesis' contradicts the number of chess amateurs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
