friends_premise = 3
friends_hypothesis = 7
rounds_premise = 7
rounds_hypothesis = 7

# the hypothesis refers to the number of friends and the number of rounds mentioned in the premise
if friends_hypothesis != friends_premise:
    # check if the number of friends in the hypothesis contradicts the number of friends reported in the premise
    label = "contradiction"
elif rounds_hypothesis != rounds_premise:
    # check if the number of rounds in the hypothesis contradicts the number of rounds reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
