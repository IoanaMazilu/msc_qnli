age_difference_premise = 6
age_difference_hypothesis = 5
age_ratio_premise = [3,4]
age_ratio_hypothesis = [3,4]

# the hypothesis refers to age difference and age ratio of Roshan and Raj mentioned in the premise
if age_difference_hypothesis >= age_difference_premise:
    # check if the age difference in the hypothesis contradicts the age difference in the premise
    label = "contradiction"
elif age_ratio_hypothesis != age_ratio_premise:
    # check if the age ratio in the hypothesis contradicts the age ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
