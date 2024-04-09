age_premise = 5/3
age_hypothesis = 1.5 * 5/3

# the hypothesis refers to the age of the speaker in the future, compared to Tom's age now
if age_hypothesis > age_premise:
    # the hypothesis explicitly entails the premise
    label = "entailment"
elif age_hypothesis < age_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise only gives an estimate of the speaker's age in the future
    # any age greater than the estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
