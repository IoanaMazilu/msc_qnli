land_size_premise = 120
land_size_hypothesis = 320

# the hypothesis refers to the land size mentioned in the premise
if land_size_premise >= land_size_hypothesis:
    # check if the estimate of 'land_size_hypothesis' contradicts the land size in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
