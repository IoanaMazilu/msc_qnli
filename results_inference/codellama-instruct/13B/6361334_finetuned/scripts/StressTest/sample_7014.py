lewis_age_premise = 1
brown_age_premise = 2
lewis_age_hypothesis = 6
brown_age_hypothesis = 2

# the hypothesis refers to the ratio of the ages of Lewis and Brown, which is also mentioned in the premise
if lewis_age_hypothesis <= lewis_age_premise and brown_age_hypothesis <= brown_age_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of the ages
    # any ratio of ages less than 'lewis_age_hypothesis' and 'brown_age_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
