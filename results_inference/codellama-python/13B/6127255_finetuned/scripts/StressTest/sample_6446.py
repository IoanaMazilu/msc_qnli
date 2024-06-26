frank_age_diff_premise = 14
frank_age_diff_hypothesis = 54

# the hypothesis talks about the age difference between Frank and John, which is also mentioned in the premise
if frank_age_diff_hypothesis!= frank_age_diff_premise:
    # check if the age difference in the hypothesis contradicts the age difference mentioned in the premise
    label = "contradiction"
else:
    # if the age difference in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)
