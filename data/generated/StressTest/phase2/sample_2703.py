# Premise: Half of the Malmo family members have blue eyes, and 4/5 of the family members who have blue eyes do not wear glasses.
# Hypothesis: Half of the Malmo family members have blue eyes, and less than 7/5 of the family members who have blue eyes do not wear glasses.
# Golden Label: entailment

blue_eyes_ratio_premise = 1/2
blue_eyes_no_glasses_ratio_premise = 4/5

blue_eyes_ratio_hypothesis = 1/2
blue_eyes_no_glasses_ratio_hypothesis = 7/5

# the hypothesis talks about the same ratios of family members with blue eyes and without glasses as in the premise
if blue_eyes_ratio_premise != blue_eyes_ratio_hypothesis:
    # check if the proportion of family members with blue eyes in the hypothesis contradicts the proportion in the premise
    label = "contradiction"
elif blue_eyes_no_glasses_ratio_hypothesis >= blue_eyes_no_glasses_ratio_premise:
    # check if the proportion of family members with blue eyes and without glasses in the hypothesis contradicts the respective proportion in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

