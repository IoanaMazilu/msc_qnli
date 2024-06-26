frank_age_difference_premise = 14
frank_age_difference_hypothesis = 84

# the hypothesis refers to the age difference between Frank and John, which is also mentioned in the premise
if frank_age_difference_hypothesis >= frank_age_difference_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
