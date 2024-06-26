land_size_premise = 120
land_size_hypothesis = 820

# the hypothesis refers to the size of the land mentioned in the premise
if land_size_hypothesis != land_size_premise:
    # check if the land size in the hypothesis contradicts the land size reported in the premise
    label = "contradiction"
else:
    # if the land size in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)
