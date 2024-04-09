frank_age_difference_premise = 14
frank_age_difference_hypothesis = 84

# the hypothesis refers to the age difference between Frank and John mentioned in the premise
if frank_age_difference_premise > frank_age_difference_hypothesis:
    # check if the estimate of 'frank_age_difference_premise' contradicts the age difference in the hypothesis
    label = "contradiction"
elif frank_age_difference_premise < frank_age_difference_hypothesis:
    # if the age difference in the hypothesis is less than the one in the premise, we can infer entailment
    label = "entailment"
else:
    # if the age difference in the hypothesis is equal to the one in the premise, it is neutral
    label = "neutral"

print(label)
