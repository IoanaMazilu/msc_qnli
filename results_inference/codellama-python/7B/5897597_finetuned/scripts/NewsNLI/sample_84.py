age_premise = 23
age_hypothesis = 23

# the hypothesis mentions the age of Gregory Rose, which is also mentioned in the premise
if age_hypothesis!= age_premise:
    # check if the age in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis age does not contradict the premise age, we can infer entailment
    label = "entailment"

print(label)
