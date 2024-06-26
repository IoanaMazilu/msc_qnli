ratios_premise = [4, 3]  # Rahul's and Deepak's ratio in the premise
ratios_hypothesis = [1, 3]  # Rahul's and Deepak's ratio in the hypothesis
rahul_age_future_premise = 26  # Rahul's future age in the premise
rahul_age_future_hypothesis = 26  # Rahul's future age in the hypothesis

# the hypothesis refers to the same ratios and future ages mentioned in the premise

# comparing Rahul's ratios in the premise and the hypothesis
if ratios_premise[0] != ratios_hypothesis[0]:
    label = "contradiction"
# comparing Deepak's ratios in the premise and the hypothesis
elif ratios_premise[1] != ratios_hypothesis[1]:
    label = "contradiction"
# comparing Rahul's future ages in the premise and the hypothesis
elif rahul_age_future_premise != rahul_age_future_hypothesis:
    label = "contradiction"
else:
    label = "entailment"

print(label)
