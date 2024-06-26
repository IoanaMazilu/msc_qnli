sameer_age_premise = 5
anand_age_premise = 4
sameer_age_hypothesis = 4
anand_age_hypothesis = 3

# the hypothesis talks about the ratio of the ages of Sameer and Anand
if sameer_age_hypothesis / anand_age_hypothesis > sameer_age_premise / anand_age_premise:
    # check if the hypothesis ratio contradicts the premise ratio
    label = "contradiction"
elif sameer_age_hypothesis / anand_age_hypothesis == sameer_age_premise / anand_age_premise:
    # check if the hypothesis ratio is consistent with the premise ratio
    label = "entailment"
else:
    # the premise gives only an estimate for the ratio of the ages
    # any ratio less than 5:4 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
