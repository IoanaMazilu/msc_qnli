# Premise: Mary is less than 56 years younger than Albert.
# Hypothesis: Mary is 16 years younger than Albert.
# Golden Label: neutral

mary_age_difference_premise = 56
mary_age_difference_hypothesis = 16

# the hypothesis refers to the age difference between Mary and Albert, also mentioned in the premise
if mary_age_difference_hypothesis > mary_age_difference_premise:
    # check if the hypothesis value contradicts the premise of being less than 'mary_age_difference_premise' years difference
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

