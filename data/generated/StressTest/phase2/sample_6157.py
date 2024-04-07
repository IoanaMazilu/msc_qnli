# Premise: Present ages of Sameer and Anand are in the ratio of more than 3:4 respectively.
# Hypothesis: Present ages of Sameer and Anand are in the ratio of 5:4 respectively.
# Golden Label: neutral

sameer_age_ratio_premise = 3
anand_age_ratio_premise = 4
sameer_age_ratio_hypothesis = 5
anand_age_ratio_hypothesis = 4

# the hypothesis refers to the ratio of ages of Sameer and Anand mentioned in the premise
if sameer_age_ratio_hypothesis <= sameer_age_ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than 'sameer_age_ratio_premise'
    label = "contradiction"
elif anand_age_ratio_hypothesis != anand_age_ratio_premise:
    # check if the ratio of Anand's age in the hypothesis contradicts the ratio of Anand's age reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of Sameer's age
    # any ratio greater than 'sameer_age_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

