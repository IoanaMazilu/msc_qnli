friends_premise = 6
combinations_premise = 2
combinations_hypothesis = 4

# the hypothesis refers to the number of combinations of passengers, which is also mentioned in the premise
if combinations_hypothesis <= combinations_premise:
    # check if the number of combinations in the hypothesis contradicts the number of combinations in the premise
    label = "contradiction"
else:
    # if the number of combinations in the hypothesis does not contradict the number of combinations in the premise, we can infer entailment
    label = "entailment"

print(label)
