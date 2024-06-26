age_ratio_premise = 3/4
age_ratio_hypothesis = 3/4
age_difference_premise = 5
age_difference_hypothesis = 2

# the hypothesis refers to the age difference between Roshan and Raj, which is also mentioned in the premise
if age_difference_hypothesis!= age_difference_premise:
    # check if the age difference in the hypothesis contradicts the age difference in the premise
    label = "contradiction"
elif age_ratio_hypothesis!= age_ratio_premise:
    # check if the age ratio in the hypothesis contradicts the age ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
