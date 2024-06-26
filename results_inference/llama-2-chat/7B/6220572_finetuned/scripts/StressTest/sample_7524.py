friends_premise = 6
friends_hypothesis = 2
combinations_premise = 4
combinations_hypothesis = 4

# the hypothesis refers to the number of combinations of passengers from the premise
if combinations_hypothesis <= combinations_premise:
    # check if the hypothesis value contradicts the number of combinations in the premise
    label = "contradiction"
elif friends_hypothesis <= friends_premise:
    # check if the number of friends in the hypothesis contradicts the number of friends reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
