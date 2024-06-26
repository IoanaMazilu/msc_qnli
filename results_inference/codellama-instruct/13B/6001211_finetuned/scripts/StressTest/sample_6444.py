frank_age_difference_premise = 14
frank_age_difference_hypothesis = 84

# the hypothesis refers to the age difference between Frank and John mentioned in the premise
if frank_age_difference_premise > frank_age_difference_hypothesis:
    # check if the age difference in the premise contradicts the age difference in the hypothesis
    label = "contradiction"
elif frank_age_difference_premise < frank_age_difference_hypothesis:
    # check if the age difference in the premise is less than the age difference in the hypothesis
    label = "entailment"
else:
    # if the age difference in the premise is equal to the age difference in the hypothesis, we can infer neutrality
    label = "neutral"

print(label)
