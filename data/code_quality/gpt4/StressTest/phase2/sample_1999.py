frank_age_difference_premise = 63
frank_age_difference_hypothesis = 13

# the hypothesis states a specific age difference between Frank and John, which is also referenced in the premise
if frank_age_difference_hypothesis > frank_age_difference_premise:
    # check if the hypothesis age difference contradicts the premise of Frank being less than 'frank_age_difference_premise' years younger
    label = "contradiction"
else:
    # if the age difference in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
