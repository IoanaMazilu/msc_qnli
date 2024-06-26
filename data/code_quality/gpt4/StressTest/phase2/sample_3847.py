friends_premise = 5
friends_hypothesis = 6

# the hypothesis refers to the number of friends mentioned in the premise
if friends_premise != friends_hypothesis:
    # check if the number of friends in the hypothesis contradicts the number of friends mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
