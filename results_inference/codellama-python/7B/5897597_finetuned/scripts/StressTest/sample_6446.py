frank_age_diff_premise = 14
frank_age_diff_hypothesis = 54

# the hypothesis refers to the age difference between Frank and John mentioned in the premise
if frank_age_diff_hypothesis!= frank_age_diff_premise:
    # check if the age difference in the hypothesis contradicts the age difference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
