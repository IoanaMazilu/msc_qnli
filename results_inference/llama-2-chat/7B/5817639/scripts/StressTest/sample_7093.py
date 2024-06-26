ratio_premise = 8
ratio_hypothesis = 5
age_premise = 26
age_hypothesis = 26

# the hypothesis talks about the ratio and age of two individuals, referenced also in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the ratio, which is consistent with the hypothesis
    # but the hypothesis does not provide any explicit information about the age
    label = "neutral"

print(label)
