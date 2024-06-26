passengers_premise = 12
passengers_hypothesis = 12

# the hypothesis refers to the number of passengers on a ship mentioned in the premise
if passengers_premise <= passengers_hypothesis:
    # check if the estimate of 'passengers_hypothesis' contradicts the number of passengers in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
