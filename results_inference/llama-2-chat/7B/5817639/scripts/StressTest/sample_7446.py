ratio_premise = 4
ratio_hypothesis = 1
age_premise = 26
age_hypothesis = 26

# the hypothesis talks about the ratio and age of two people, referenced also in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the ratio, and the hypothesis value is consistent with it
    label = "entailment"

if age_hypothesis <= age_premise:
    # check if the hypothesis value contradicts the estimate of the age in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the age, and the hypothesis value is consistent with it
    label = "entailment"

print(label)
