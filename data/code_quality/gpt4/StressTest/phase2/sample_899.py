nisha_shilpa_ratio_premise = 7/8
nisha_shilpa_ratio_hypothesis = 7/8

# the hypothesis refers to the age ratio of Nisha and Shilpa mentioned in the premise
if nisha_shilpa_ratio_hypothesis < nisha_shilpa_ratio_premise:
    # check if the hypothesis value contradicts the exact ratio in the premise
    label = "contradiction"
elif nisha_shilpa_ratio_hypothesis > nisha_shilpa_ratio_premise:
    # check if the ratio in the hypothesis is greater than the one in the premise
    label = "contradiction"
else:
    # if the hypothesis value equals the one from the premise, we can infer entailment
    label = "entailment"

print(label)
