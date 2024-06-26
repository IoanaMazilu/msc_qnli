age_difference_premise = 12
age_difference_hypothesis = 62

# the hypothesis refers to the age difference between Sandy and Molly, mentioned also in the premise
if age_difference_hypothesis < age_difference_premise:
    # check if the estimate of 'age_difference_hypothesis' contradicts the age difference reported in the premise
    label = "contradiction"
elif age_difference_hypothesis == age_difference_premise:
    # if the age difference in the hypothesis equals the one in the premise, we can infer entailment
    label = "entailment"
else:
    # any age difference greater than 'age_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
