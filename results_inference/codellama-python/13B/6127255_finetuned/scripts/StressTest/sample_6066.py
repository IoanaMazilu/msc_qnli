shops_premise_min = 4
shops_premise_max = 5
shops_hypothesis_min = 5
shops_hypothesis_max = 5

# the hypothesis refers to the number of shops in the town mentioned in the premise
if shops_hypothesis_min >= shops_premise_min and shops_hypothesis_max >= shops_premise_max:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
elif shops_hypothesis_min < shops_premise_min and shops_hypothesis_max < shops_premise_max:
    # check if the hypothesis values are less than the premise ones
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict or are less than the premise ones, we can infer neutrality
    label = "neutral"

print(label)
