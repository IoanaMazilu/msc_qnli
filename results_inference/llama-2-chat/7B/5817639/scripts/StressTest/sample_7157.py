age_ratio_premise = 4
age_ratio_hypothesis = 5

# the hypothesis talks about a ratio that is greater than the ratio mentioned in the premise
if age_ratio_hypothesis <= age_ratio_premise:
    # check if the estimate of 'age_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise provides only a lower bound for the ratio, and any ratio greater than that is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
