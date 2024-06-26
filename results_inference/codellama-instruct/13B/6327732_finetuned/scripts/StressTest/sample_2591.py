sameer_age_premise = 5
anand_age_premise = 4
sameer_age_hypothesis = 4
anand_age_hypothesis = 3

# the hypothesis refers to the ratio of the ages of Sameer and Anand
if sameer_age_hypothesis <= sameer_age_premise and anand_age_hypothesis <= anand_age_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives an explicit ratio for the ages of Sameer and Anand
    # any ratio less than 5:4 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
