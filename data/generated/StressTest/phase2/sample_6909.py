# Premise: Roshan is 5 years younger than Raj and they have an age ratio 3:4 respectively.
# Hypothesis: Roshan is less than 6 years younger than Raj and they have an age ratio 3:4 respectively.
# Golden Label: entailment

roshan_age_diff_premise = 5
roshan_age_diff_hypothesis = 6
age_ratio_premise = [3, 4]
age_ratio_hypothesis = [3, 4]

# the hypothesis refers to the age difference and ratio between Roshan and Raj mentioned in the premise
if roshan_age_diff_premise > roshan_age_diff_hypothesis:
    # check if the estimate of 'roshan_age_diff_hypothesis' contradicts the age difference in the premise
    label = "contradiction"
elif age_ratio_hypothesis != age_ratio_premise:
    # check if the age ratio in the hypothesis contradicts the age ratio reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
