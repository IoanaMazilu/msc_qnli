# Premise: Mary is 10 years younger than Albert.
# Hypothesis: Mary is 20 years younger than Albert.
# Golden Label: contradiction

mary_age_difference_premise = 10
mary_age_difference_hypothesis = 20

# the hypothesis refers to Mary's age difference with Albert, also mentioned in the premise
if mary_age_difference_hypothesis != mary_age_difference_premise:
    # check if the age difference in the hypothesis contradicts the age difference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis age difference doesn't contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

