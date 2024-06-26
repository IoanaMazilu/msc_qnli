age_ratio_premise = 5/4
age_ratio_hypothesis = 3/4

# the hypothesis talks about the ratio of ages of two people, referenced also in the premise
if age_ratio_hypothesis <= age_ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio of ages in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the ratio of ages, and the hypothesis value is consistent with that estimate
    label = "entailment"

print(label)
