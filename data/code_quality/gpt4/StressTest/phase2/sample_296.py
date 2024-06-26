frank_age_difference_premise = 12
frank_age_difference_hypothesis = 12

# the hypothesis refers to the age difference between Frank and John mentioned in the premise
if frank_age_difference_hypothesis < frank_age_difference_premise:
    # check if the hypothesis value contradicts the age difference stated in the premise
    label = "contradiction"
elif frank_age_difference_hypothesis > frank_age_difference_premise:
    # check if the hypothesis value contradicts the age difference stated in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
