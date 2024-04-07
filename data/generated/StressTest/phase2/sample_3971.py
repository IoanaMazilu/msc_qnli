# Premise: Mary is 16 years younger than Albert.
# Hypothesis: Mary is 36 years younger than Albert.
# Golden Label: contradiction

mary_age_difference_premise = 16
mary_age_difference_hypothesis = 36

# the hypothesis refers to the difference in age between Mary and Albert as stated in the premise
if mary_age_difference_hypothesis != mary_age_difference_premise:
    # check if the age difference in the hypothesis contradicts the age difference stated in the premise
    label = "contradiction"
else:
    # if the age difference in the hypothesis matches the age difference in the premise, we can infer entailment
    label = "entailment"

print(label)

