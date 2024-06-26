efficiency_premise = 0.10
efficiency_hypothesis = 0.09

# the hypothesis refers to the efficiency of Rosy compared to Mary
if efficiency_hypothesis > efficiency_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif efficiency_premise!= efficiency_hypothesis:
    # check if the hypothesis value does not contradict the premise value
    label = "neutral"
else:
    # if the hypothesis value is consistent with the premise value, we can infer entailment
    label = "entailment"

print(label)
