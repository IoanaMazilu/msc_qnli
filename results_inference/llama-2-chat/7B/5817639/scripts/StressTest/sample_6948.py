age_premise = 5
age_hypothesis = 1

# the hypothesis talks about the ratio of the ages of two people, referenced also in the premise
if age_hypothesis <= age_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio, any ratio greater than 1:4 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
