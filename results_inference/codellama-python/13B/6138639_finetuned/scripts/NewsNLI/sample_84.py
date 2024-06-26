age_premise = 23
age_hypothesis = 23

# the hypothesis mentions the age at which Gregory Rose was diagnosed with leukemia, which is also mentioned in the premise
if age_hypothesis!= age_premise:
    # check if the age in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
