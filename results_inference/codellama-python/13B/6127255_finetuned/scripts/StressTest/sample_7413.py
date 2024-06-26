land_size_premise = 120
land_size_hypothesis = 320

# the hypothesis refers to the size of the land mentioned in the premise
if land_size_premise >= land_size_hypothesis:
    # check if the size of the land in the premise contradicts the estimate of less than 'land_size_hypothesis'
    label = "contradiction"
else:
    # if the land size in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
