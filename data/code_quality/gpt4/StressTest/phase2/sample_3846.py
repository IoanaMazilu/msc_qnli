friends_premise = 6
friends_hypothesis = 5

# the hypothesis refers to the number of friends mentioned in the premise
if friends_premise > friends_hypothesis:
    # check if the number of friends in the hypothesis contradicts the number of friends in the premise
    label = "contradiction"
else:
    # if the hypothesis value doesn't contradict the premise, we can infer entailment
    label = "entailment"

print(label)
