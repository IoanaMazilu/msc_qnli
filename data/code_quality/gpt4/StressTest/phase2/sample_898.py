nisha_shilpa_ratio_premise = 3/8
nisha_shilpa_ratio_hypothesis = 7/8

# The hypothesis talks about the ratio of ages of Nisha and Shilpa, which is also referenced in the premise
if nisha_shilpa_ratio_hypothesis <= nisha_shilpa_ratio_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'nisha_shilpa_ratio_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the ratio of ages
    # Any ratio greater than 'nisha_shilpa_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
