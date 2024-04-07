# Premise: Roshan is 5 years younger than Raj and they have an age ratio 3:4 respectively.
# Hypothesis: Roshan is 2 years younger than Raj and they have an age ratio 3:4 respectively.
# Golden Label: contradiction

roshan_age_difference_premise = 5
roshan_age_difference_hypothesis = 2
age_ratio_premise = [3, 4]
age_ratio_hypothesis = [3, 4]

# the hypothesis refers to the age difference and ratio between Roshan and Raj, also mentioned in the premise
if roshan_age_difference_premise != roshan_age_difference_hypothesis:
    # check if the age difference in the hypothesis contradicts the age difference in the premise
    label = "contradiction"
elif age_ratio_premise != age_ratio_hypothesis:
    # check if the age ratio in the hypothesis contradicts the age ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

