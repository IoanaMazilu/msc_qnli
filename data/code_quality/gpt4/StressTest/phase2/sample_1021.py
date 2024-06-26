combinations_premise = 8
combinations_hypothesis = 2
friends_premise = 4
friends_hypothesis = 4

# the hypothesis refers to the number of combinations and friends mentioned in the premise
if combinations_hypothesis >= combinations_premise:
    # check if the number of combinations in the hypothesis contradicts the premise's number of less than 'combinations_premise'
    label = "contradiction"
elif friends_hypothesis != friends_premise:
    # check if the number of friends in the hypothesis contradicts the number of friends mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
