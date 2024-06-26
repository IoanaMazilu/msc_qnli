oil_per_cylinder_premise = 8
oil_per_cylinder_hypothesis = 7

# the hypothesis refers to the amount of oil needed for each cylinder, as mentioned in the premise
if oil_per_cylinder_premise <= oil_per_cylinder_hypothesis:
    # check if the estimate of 'oil_per_cylinder_hypothesis' contradicts the amount of oil needed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
