lewis_age_premise = 6
brown_age_premise = 2
lewis_age_hypothesis = 1
brown_age_hypothesis = 2

# the hypothesis refers to the ratio of the ages of Lewis and Brown, which is also mentioned in the premise
if lewis_age_hypothesis <= lewis_age_premise and brown_age_hypothesis <= brown_age_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of the ages
    # any ratio of the ages greater than 'lewis_age_premise:brown_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
