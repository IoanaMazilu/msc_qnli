age_ratio_premise = 5/3
age_ratio_hypothesis = 5/3

# the hypothesis refers to the age ratio mentioned in the premise
if age_ratio_hypothesis <= age_ratio_premise:
    # check if the hypothesis value contradicts the age ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
