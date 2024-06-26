efficiency_premise = 10
efficiency_hypothesis = 30

# the hypothesis refers to the efficiency difference between Rosy and Mary mentioned in the premise
if efficiency_hypothesis <= efficiency_premise:
    # check if the estimate of 'efficiency_hypothesis' contradicts the efficiency difference in the premise
    label = "contradiction"
elif efficiency_hypothesis > efficiency_premise:
    # check if the efficiency difference in the hypothesis is more than the one reported in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
