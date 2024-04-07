# Premise: The ratio of present ages of Nisha and Shilpa is 7:8 respectively.
# Hypothesis: The ratio of present ages of Nisha and Shilpa is more than 3:8 respectively.
# Golden Label: entailment

nisha_shilpa_ratio_premise = 7 / 8
nisha_shilpa_ratio_hypothesis = 3 / 8

# the hypothesis talks about the ratio of Nisha and Shilpa's age, which is also mentioned in the premise
if nisha_shilpa_ratio_hypothesis >= nisha_shilpa_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives a specific ratio for the ages of Nisha and Shilpa
    # any ratio less than 'nisha_shilpa_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

