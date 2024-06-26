age_premise = 5/3
age_hypothesis = 5/3

# the hypothesis refers to the same ratio of age as the premise
if age_hypothesis <= age_premise:
    # check if the estimate of 'age_hypothesis' contradicts the ratio of age in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of age
    # any ratio of age greater than 'age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
