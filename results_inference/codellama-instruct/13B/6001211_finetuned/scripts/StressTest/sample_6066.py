shops_premise_min = 4
shops_premise_max = 5
shops_hypothesis_min = 5
shops_hypothesis_max = 5

# the hypothesis refers to the number of shops in the town mentioned in the premise
if shops_hypothesis_min >= shops_premise_min and shops_hypothesis_max <= shops_premise_max:
    # check if the estimate of'shops_hypothesis_min' contradicts the number of shops in the premise
    label = "contradiction"
elif shops_hypothesis_min > shops_premise_min and shops_hypothesis_max > shops_premise_max:
    # check if the number of shops in the hypothesis contradicts the number of shops reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
