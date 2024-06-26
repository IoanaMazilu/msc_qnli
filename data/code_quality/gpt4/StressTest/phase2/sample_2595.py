efficiency_difference_premise = 30
efficiency_difference_hypothesis = 10

# the hypothesis refers to the efficiency difference between Rosy and Mary mentioned in the premise
if efficiency_difference_premise <= efficiency_difference_hypothesis:
    # check if the estimate of 'efficiency_difference_hypothesis' contradicts the efficiency difference in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
