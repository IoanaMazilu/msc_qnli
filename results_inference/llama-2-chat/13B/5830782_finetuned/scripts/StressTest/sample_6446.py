frank_age_diff_premise = 40
frank_age_diff_hypothesis = 54

# the hypothesis refers to the age difference between Frank and John mentioned in the premise
if frank_age_diff_premise!= frank_age_diff_hypothesis:
    # check if the age difference in the hypothesis contradicts the age difference reported in the premise
    label = "contradiction"
else:
    # if the age difference in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
