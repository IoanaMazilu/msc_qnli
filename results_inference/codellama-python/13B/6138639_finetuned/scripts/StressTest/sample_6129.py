hours_premise = 21
hours_hypothesis = 11

# the hypothesis refers to the number of hours Harry works per week, mentioned in the premise
if hours_premise <= hours_hypothesis:
    # check if the estimate of 'hours_hypothesis' contradicts the number of hours in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
