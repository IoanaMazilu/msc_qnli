sold_value_premise = 450
sold_value_hypothesis = 750

# the hypothesis refers to the value sold to George mentioned in the premise
if sold_value_premise >= sold_value_hypothesis:
    # check if the estimate of'sold_value_hypothesis' contradicts the value sold in the premise
    label = "contradiction"
elif sold_value_hypothesis < sold_value_premise:
    # check if the value sold in the hypothesis contradicts the value sold in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
