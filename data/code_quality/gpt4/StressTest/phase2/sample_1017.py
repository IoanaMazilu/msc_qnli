friends_premise = 4
friends_hypothesis = 8

# the hypothesis refers to the number of John's friends mentioned in the premise
if friends_hypothesis <= friends_premise:
    # check if the estimate of 'friends_hypothesis' contradicts the number of John's friends in the premise
    label = "contradiction"
elif friends_hypothesis != friends_premise:
    # the hypothesis gives only an estimate for the number of John's friends
    # any number of friends less than 'friends_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
