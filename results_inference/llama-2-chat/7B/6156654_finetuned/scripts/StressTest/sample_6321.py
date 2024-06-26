chess_amateurs_premise = 4
chess_amateurs_hypothesis = 8

# the hypothesis refers to the number of chess amateurs playing in Villa's chess club tournament, which is also mentioned in the premise
if chess_amateurs_premise >= chess_amateurs_hypothesis:
    # check if the number of chess amateurs in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the number of chess amateurs in the premise is less than the hypothesis, we can infer entailment
    label = "entailment"

print(label)
