shops_premise_lower = 4
shops_premise_upper = 5
shops_hypothesis_lower = 4
shops_hypothesis_upper = 5

# the hypothesis refers to the number of shops in the town mentioned in the premise
if shops_hypothesis_lower >= shops_premise_lower and shops_hypothesis_upper <= shops_premise_upper:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
