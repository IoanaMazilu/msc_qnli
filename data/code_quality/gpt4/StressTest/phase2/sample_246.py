# Ratio of Rahul and Deepak's age in premise and hypothesis
ratio_premise_rahul = 4
ratio_premise_deepak = 3

ratio_hypothesis_rahul = 2
ratio_hypothesis_deepak = 3

# Rahul's age after 6 years in premise and hypothesis
rahul_age_future_premise = 26
rahul_age_future_hypothesis = 26

# Compare the ratio of Rahul and Deepak's age in the premise to the hypothesis
if ratio_premise_rahul / ratio_premise_deepak <= ratio_hypothesis_rahul / ratio_hypothesis_deepak:
    # Check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif rahul_age_future_premise != rahul_age_future_hypothesis:
    # Check if Rahul's future age in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
