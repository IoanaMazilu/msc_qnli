roshan_age_premise = 5 * 3 = 15
raj_age_premise = 3 * 4 = 12
age_ratio_premise = 3 / 4

roshan_age_hypothesis = 6 * 3 = 18
raj_age_hypothesis = 3 * 4 = 12
age_ratio_hypothesis = 3 / 4

# the hypothesis talks about the age of Roshan and Raj, and the age ratio between them
if roshan_age_hypothesis <= roshan_age_premise and raj_age_hypothesis <= raj_age_premise:
    # check if the hypothesis values do not contradict the premise values
    label = "neutral"
elif age_ratio_hypothesis == age_ratio_premise:
    # check if the hypothesis value is consistent with the premise value
    label = "entailment"
else:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"

print(label)
