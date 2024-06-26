shops_premise_lower = 4
shops_premise_upper = 5
shops_hypothesis_lower = 4
shops_hypothesis_upper = 5

# the hypothesis refers to the number of shops in the town mentioned in the premise
if shops_hypothesis_lower >= shops_premise_lower:
    # check if the estimate of'shops_hypothesis_lower' contradicts the number of shops in the premise
    label = "contradiction"
elif shops_hypothesis_upper!= shops_premise_upper:
    # check if the number of shops in the hypothesis contradicts the number of shops reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
