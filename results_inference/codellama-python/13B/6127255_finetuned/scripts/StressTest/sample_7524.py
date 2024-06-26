passengers_premise = 4
friends_premise = 6
passengers_hypothesis = 2

# the hypothesis refers to the number of passengers and friends mentioned in the premise
if passengers_hypothesis >= passengers_premise:
    # check if the number of 'passengers_hypothesis' contradicts the number of passengers in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
