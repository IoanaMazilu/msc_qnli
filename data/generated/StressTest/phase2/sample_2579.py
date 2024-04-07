# Premise: Carlos is 8 years old.
# Hypothesis: Carlos is 3 years old.
# Golden Label: contradiction

carlos_age_premise = 8
carlos_age_hypothesis = 3

# the hypothesis talks about Carlos's age, which is also mentioned in the premise
if carlos_age_hypothesis != carlos_age_premise:
    # check if the age in the hypothesis contradicts the age in the premise
    label = "contradiction"
else:
    # if the age in the hypothesis matches the age in the premise, we can infer entailment
    label = "entailment"

print(label)

