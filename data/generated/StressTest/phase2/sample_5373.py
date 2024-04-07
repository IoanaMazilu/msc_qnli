# Premise: Mary is 10 years younger than Albert.
# Hypothesis: Mary is less than 40 years younger than Albert.
# Golden Label: entailment

mary_age_difference_premise = 10
mary_age_difference_hypothesis = 40

# the hypothesis refers to the age difference between Mary and Albert mentioned in the premise
if mary_age_difference_hypothesis < mary_age_difference_premise:
    # check if the 'mary_age_difference_hypothesis' contradicts the age difference in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

