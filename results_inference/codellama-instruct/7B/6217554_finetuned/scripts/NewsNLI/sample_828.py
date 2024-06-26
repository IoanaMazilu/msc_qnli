age_premise = 34
age_hypothesis = 34

# the hypothesis mentions the age of the person, which is also referenced in the premise
if age_hypothesis!= age_premise:
    # check if the age in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
