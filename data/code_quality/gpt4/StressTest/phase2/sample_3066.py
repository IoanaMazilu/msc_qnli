mary_age_difference_premise = 14
mary_age_difference_hypothesis = 24

# the hypothesis refers to the age difference between Mary and Albert also mentioned in the premise
if mary_age_difference_hypothesis < mary_age_difference_premise:
    # check if the hypothesis value contradicts the age difference mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, it can be inferred as entailment
    label = "entailment"

print(label)
