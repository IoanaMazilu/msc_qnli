# Premise: Half of the Malmo family members have blue eyes, and less than 7/5 of the family members who have blue eyes do not wear glasses.
# Hypothesis: Half of the Malmo family members have blue eyes, and 4/5 of the family members who have blue eyes do not wear glasses.
# Golden Label: neutral

blue_eyes_premise = 1/2
blue_eyes_hypothesis = 1/2
non_glasses_wearers_premise = 7/5
non_glasses_wearers_hypothesis = 4/5

# the hypothesis refers to the number of family members having blue eyes and not wearing glasses, both mentioned in the premise
if blue_eyes_premise != blue_eyes_hypothesis:
    # check if the fraction of family members with blue eyes in the hypothesis contradicts the fraction reported in the premise
    label = "contradiction"
elif non_glasses_wearers_hypothesis > non_glasses_wearers_premise:
    # check if the fraction of non-glasses wearers in the hypothesis contradicts the premise estimate
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

