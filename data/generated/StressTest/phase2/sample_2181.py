# Premise: Frank is 15 years younger then John.
# Hypothesis: Frank is less than 75 years younger then John.
# Golden Label: entailment

frank_age_difference_premise = 15
frank_age_difference_hypothesis = 75

# the hypothesis refers to the age difference between Frank and John mentioned in the premise
if frank_age_difference_hypothesis < frank_age_difference_premise:
    # check if the hypothesis value contradicts the age difference stated in the premise
    label = "contradiction"
elif frank_age_difference_hypothesis != frank_age_difference_premise:
    # the hypothesis gives a greater value for the age difference than the premise
    # this value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the age difference in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

