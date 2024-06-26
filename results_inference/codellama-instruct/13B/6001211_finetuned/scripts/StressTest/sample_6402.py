components_premise = 60
components_hypothesis = 30

# the hypothesis refers to the number of components that a factory must manufacture, mentioned in the premise
if components_premise <= components_hypothesis:
    # check if the estimate of 'components_hypothesis' contradicts the number of components in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
