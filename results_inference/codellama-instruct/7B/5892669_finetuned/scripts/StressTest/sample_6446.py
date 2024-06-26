frank_age_difference_premise = 14
frank_age_difference_hypothesis = 54

# the hypothesis refers to the age difference between Frank and John mentioned in the premise
if frank_age_difference_hypothesis!= frank_age_difference_premise:
    # check if the age difference in the hypothesis contradicts the age difference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
