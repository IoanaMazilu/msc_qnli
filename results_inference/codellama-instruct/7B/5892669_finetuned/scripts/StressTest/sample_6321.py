chess_amateurs_premise = 4
chess_amateurs_hypothesis = 8

# the hypothesis refers to the number of chess amateurs mentioned in the premise
if chess_amateurs_premise >= chess_amateurs_hypothesis:
    # check if the number of 'chess_amateurs_premise' contradicts the estimate of less than 'chess_amateurs_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
