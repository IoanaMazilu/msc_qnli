friends_premise = 6
friends_hypothesis = 5

# the hypothesis refers to the number of John's friends mentioned in the premise
if friends_premise <= friends_hypothesis:
    # check if the number of 'friends_hypothesis' contradicts the number of friends in the premise
    label = "contradiction"
else:
    # if the number of friends in the hypothesis does not contradict the number of friends in the premise, we can infer entailment
    label = "entailment"

print(label)
