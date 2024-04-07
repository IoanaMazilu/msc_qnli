# Premise: Frank is 13 years younger then John.
# Hypothesis: Frank is 53 years younger then John.
# Golden Label: contradiction

frank_age_diff_premise = 13
frank_age_diff_hypothesis = 53

# the hypothesis refers to the age difference between Frank and John mentioned in the premise
if frank_age_diff_premise != frank_age_diff_hypothesis:
    # check if the age difference in the hypothesis contradicts the age difference stated in the premise
    label = "contradiction"
else:
    # if the age difference in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

