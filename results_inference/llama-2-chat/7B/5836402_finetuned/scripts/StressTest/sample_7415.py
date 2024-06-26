land_size_premise = 120
land_size_hypothesis = 220

# the hypothesis refers to the size of the land mentioned in the premise
if land_size_premise!= land_size_hypothesis:
    # check if the land size in the hypothesis contradicts the land size reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
