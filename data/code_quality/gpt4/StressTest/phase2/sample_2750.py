age_diff_premise = 16
age_diff_hypothesis = 36

# the hypothesis talks about the age difference between Sandy and Molly, referenced also in the premise
if age_diff_hypothesis != age_diff_premise:
    # check if the age difference in the hypothesis contradicts the age difference mentioned in the premise
    label = "contradiction"
else:
    # if the age difference in the hypothesis does not contradict the one from the premise, we can infer entailment
    label = "entailment"

print(label)
