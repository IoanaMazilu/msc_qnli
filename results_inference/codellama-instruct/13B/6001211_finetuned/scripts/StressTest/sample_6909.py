roshan_age_difference_premise = 5
roshan_age_difference_hypothesis = 6

# the hypothesis refers to the age difference between Roshan and Raj mentioned in the premise
if roshan_age_difference_hypothesis < roshan_age_difference_premise:
    # check if the estimate of 'roshan_age_difference_hypothesis' contradicts the age difference in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
