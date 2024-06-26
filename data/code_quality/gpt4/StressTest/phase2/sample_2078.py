age_diff_premise = 14
age_diff_hypothesis = 14

# the hypothesis talks about the age difference between Sandy and Molly, referenced also in the premise
if age_diff_hypothesis != age_diff_premise:
    # check if the hypothesis value contradicts the exact age difference in the premise
    label = "contradiction"
else:
    # if the age difference in the hypothesis matches the age difference in the premise, we can infer entailment
    label = "entailment"

print(label)
