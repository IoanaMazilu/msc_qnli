# Premise: Present ages of Sameer and Anand are in the ratio of 5:4 respectively.
# Hypothesis: Present ages of Sameer and Anand are in the ratio of less than 6:4 respectively.
# Golden Label: entailment

sameer_anand_ratio_premise = 5/4
sameer_anand_ratio_hypothesis = 6/4

# the hypothesis talks about the ratio of ages of Sameer and Anand, which is also mentioned in the premise
if sameer_anand_ratio_hypothesis <= sameer_anand_ratio_premise:
    # check if the hypothesis value contradicts the ratio of 'sameer_anand_ratio_premise'
    label = "contradiction"
else:
    # the premise gives a specific ratio for the ages of Sameer and Anand
    # any ratio less than 'sameer_anand_ratio_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

