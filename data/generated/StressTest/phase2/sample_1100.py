# Premise: John has 6 friends who want to ride in his new car that can accommodate only 3 people at a time (John plus 2 passengers)
# Hypothesis: John has more than 6 friends who want to ride in his new car that can accommodate only 3 people at a time (John plus 2 passengers)
# Golden Label: contradiction

friends_premise = 6
friends_hypothesis = 6

# the hypothesis refers to the number of John's friends mentioned in the premise
if friends_hypothesis <= friends_premise:
    # check if the statement 'friends_hypothesis' contradicts the number of friends reported in the premise
    label = "contradiction"
elif friends_hypothesis > friends_premise:
    # check if the number of friends in the hypothesis contradicts the number of friends reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

