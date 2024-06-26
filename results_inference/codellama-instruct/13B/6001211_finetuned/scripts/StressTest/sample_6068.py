shops_premise_min = 4
shops_premise_max = 5
shops_hypothesis_max = 4

# the hypothesis refers to the number of shops in the town mentioned in the premise
if shops_hypothesis_max >= shops_premise_min:
    # check if the estimate of'shops_hypothesis_max' contradicts the number of shops in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
