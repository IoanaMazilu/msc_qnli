components_premise = 30
components_hypothesis = 60

# the hypothesis refers to the number of components mentioned in the premise
if components_hypothesis!= components_premise:
    # check if the number of components in the hypothesis contradicts the number of components reported in the premise
    label = "contradiction"
elif (components_hypothesis * 0.8)!= (components_premise * 0.8):
    # check if the percentage of components that would be most efficiently manufactured by Machine A in the hypothesis contradicts the percentage of components that would be most efficiently manufactured by Machine A in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
