mary_age_difference_premise = 12
mary_age_difference_hypothesis = 12

# the hypothesis refers to the age difference between Mary and Albert mentioned in the premise
if mary_age_difference_hypothesis < mary_age_difference_premise:
    # check if the age difference in the hypothesis contradicts the age difference reported in the premise
    label = "contradiction"
elif mary_age_difference_hypothesis > mary_age_difference_premise:
    # check if the age difference in the hypothesis contradicts the age difference reported in the premise
    label = "contradiction"
else:
    # if the age difference in the hypothesis does not contradict the age difference in the premise, we can infer entailment
    label = "entailment"

print(label)
