frank_age_difference_premise = 14
frank_age_difference_hypothesis = 54

# the hypothesis refers to the age difference between Frank and John mentioned in the premise
if frank_age_difference_premise!= frank_age_difference_hypothesis:
    # check if the age difference in the hypothesis contradicts the age difference in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
