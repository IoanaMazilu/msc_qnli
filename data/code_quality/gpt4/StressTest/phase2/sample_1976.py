friends_premise = 7
friends_hypothesis = 8

# the hypothesis refers to the number of Julie's friends mentioned in the premise
if friends_hypothesis != friends_premise:
    # check if the number of friends in the hypothesis contradicts the number of friends reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
