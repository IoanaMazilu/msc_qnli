frank_age_diff_premise = 14
frank_age_diff_hypothesis = 84

# the hypothesis refers to the age difference between Frank and John mentioned in the premise
if frank_age_diff_premise > frank_age_diff_hypothesis:
    # check if the age difference in the premise contradicts the hypothesis that Frank is less than 84 years younger
    label = "contradiction"
else:
    # if the age difference in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
