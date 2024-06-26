age_premise = 6
age_hypothesis = 4

# the hypothesis talks about Sandy's age in the future, referenced also in the premise
if age_hypothesis <= age_premise:
    # check if the hypothesis age contradicts the premise age
    label = "contradiction"
else:
    # the premise gives an estimate for Sandy's age in the future, but the hypothesis age is not necessarily inconsistent with that estimate
    label = "neutral"

print(label)
