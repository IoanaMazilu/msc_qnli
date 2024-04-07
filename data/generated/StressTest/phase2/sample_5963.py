# Premise: Present ages of Sameer and Anand are in the ratio of 5:4 respectively.
# Hypothesis: Present ages of Sameer and Anand are in the ratio of more than 5:4 respectively.
# Golden Label: contradiction

sameer_anand_ratio_premise = 5/4
sameer_anand_ratio_hypothesis = 5/4

# the hypothesis refers to the age ratio of Sameer and Anand mentioned in the premise
if sameer_anand_ratio_hypothesis <= sameer_anand_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an exact ratio for the ages of Sameer and Anand
    # any ratio greater than 'sameer_anand_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

