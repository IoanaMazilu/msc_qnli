# Premise: Mary is 14 years younger than Albert.
# Hypothesis: Mary is 34 years younger than Albert.
# Golden Label: contradiction

mary_age_difference_premise = 14
mary_age_difference_hypothesis = 34

# the hypothesis refers to the age difference between Mary and Albert mentioned in the premise
if mary_age_difference_hypothesis != mary_age_difference_premise:
    # check if the age difference in the hypothesis contradicts the age difference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

