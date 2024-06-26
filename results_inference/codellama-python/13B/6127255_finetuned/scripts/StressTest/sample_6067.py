shops_premise_min = 5
shops_premise_max = 5
shops_hypothesis_min = 4
shops_hypothesis_max = 5

# the hypothesis refers to the number of shops in the town mentioned in the premise
if shops_hypothesis_min >= shops_premise_min and shops_hypothesis_max == shops_premise_max:
    # check if the number of shops in the hypothesis contradicts the estimate of less than'shops_premise_min'
    label = "contradiction"
elif shops_hypothesis_min < shops_premise_min and shops_hypothesis_max == shops_premise_max:
    # the premise gives only an estimate for the number of shops
    # any number of shops less than'shops_premise_min' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
