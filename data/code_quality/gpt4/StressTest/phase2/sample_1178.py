lower_bound_premise = 1
upper_bound_premise = 10
lower_bound_hypothesis = 5
upper_bound_hypothesis = 10

# the hypothesis refers to the range of integer generation mentioned in the premise
if lower_bound_hypothesis < lower_bound_premise or upper_bound_hypothesis > upper_bound_premise:
    # check if the bounds of integer generation in the hypothesis contradict the bounds in the premise
    label = "contradiction"
elif lower_bound_hypothesis == lower_bound_premise and upper_bound_hypothesis == upper_bound_premise:
    # check if the bounds of integer generation in the hypothesis exactly match the bounds in the premise
    label = "entailment"
else:
    # the bounds of integer generation in the hypothesis are within the bounds in the premise, 
    # but cannot be explicitly derived from the premise
    label = "neutral"

print(label)
