rajan_age_difference_premise = 5
rajan_age_difference_hypothesis = 6
age_ratio_premise = 3/4
age_ratio_hypothesis = 3/4

# the hypothesis refers to the age difference between Raj and Roshan and their age ratio, mentioned in the premise
if rajan_age_difference_hypothesis <= rajan_age_difference_premise:
    # check if the hypothesis value contradicts the age difference in the premise
    label = "contradiction"
elif age_ratio_hypothesis!= age_ratio_premise:
    # check if the age ratio in the hypothesis contradicts the age ratio reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
