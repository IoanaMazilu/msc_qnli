# Premise: Sandy is younger than Molly by 12 years.
# Hypothesis: Sandy is younger than Molly by 22 years.
# Golden Label: contradiction

age_diff_premise = 12
age_diff_hypothesis = 22

# the hypothesis talks about the age difference between Sandy and Molly, which is also discussed in the premise
if age_diff_hypothesis != age_diff_premise:
    # check if the age difference in the hypothesis contradicts the age difference stated in the premise
    label = "contradiction"
else:
    # if the age difference in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

