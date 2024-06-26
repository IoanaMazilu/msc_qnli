sunil_age_difference_premise = 4
sunil_age_difference_hypothesis = 6

# the hypothesis refers to the difference in age between Sunil and Syam mentioned in the premise
if sunil_age_difference_premise != sunil_age_difference_hypothesis:
    # check if the difference in age in the hypothesis contradicts the difference in age reported in the premise
    label = "contradiction"
else:
    # if the difference in age in the hypothesis does not contradict the difference in age in the premise, we can infer entailment
    label = "entailment"

print(label)
