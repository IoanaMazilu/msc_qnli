age_premise = 7
age_hypothesis = 1

# the hypothesis refers to the ratio of the ages of Anil and his son mentioned in the premise
if age_hypothesis <= age_premise:
    # check if the estimate of 'age_hypothesis' contradicts the ratio of ages in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of ages
    # any ratio of ages greater than 'age_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
