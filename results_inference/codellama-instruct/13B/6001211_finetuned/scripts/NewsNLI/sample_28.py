earning_premise = 29.3
earning_hypothesis = 29.3

# the hypothesis mentions the earning of The Lion King 3D, which is also mentioned in the premise
if earning_hypothesis!= earning_premise:
    # check if the earning in the hypothesis contradicts the earning reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
