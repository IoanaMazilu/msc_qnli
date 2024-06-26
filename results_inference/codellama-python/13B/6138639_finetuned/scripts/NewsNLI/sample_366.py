gunshots_premise = 10
gunshots_hypothesis = 10

# the hypothesis mentions the number of gunshots, which is also mentioned in the premise
if gunshots_hypothesis!= gunshots_premise:
    # check if the number of gunshots in the hypothesis contradicts the number of gunshots reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
