# Premise: Half of the Malmo family members have blue eyes, and 4/5 of the family members who have blue eyes do not wear glasses.
# Hypothesis: Half of the Malmo family members have blue eyes, and more than 4/5 of the family members who have blue eyes do not wear glasses.
# Golden Label: contradiction

blue_eyes_ratio_premise = 1/2
blue_eyes_ratio_hypothesis = 1/2

glasses_ratio_premise = 4/5
glasses_ratio_hypothesis = 4/5

# the hypothesis refers to the same ratios of family members with blue eyes and those who do not wear glasses as the premise
if blue_eyes_ratio_hypothesis != blue_eyes_ratio_premise:
    # check if the ratio of family members with blue eyes in the hypothesis contradicts the ratio reported in the premise
    label = "contradiction"
elif glasses_ratio_hypothesis <= glasses_ratio_premise:
    # check if the ratio of family members with blue eyes who do not wear glasses in the hypothesis contradicts the ratio reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of family members with blue eyes who do not wear glasses
    # any ratio higher than 'glasses_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

