shops_premise = 4
shops_hypothesis = 4

# the hypothesis refers to the number of shops in the town mentioned in the premise
if shops_hypothesis >= shops_premise:
    # check if the hypothesis value contradicts the estimate of less than'shops_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
