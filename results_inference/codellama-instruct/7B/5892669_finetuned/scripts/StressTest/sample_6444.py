frank_age_difference_premise = 14
frank_age_difference_hypothesis = 84

# the hypothesis refers to the age difference between Frank and John mentioned in the premise
if frank_age_difference_premise > frank_age_difference_hypothesis:
    # check if the age difference in the premise contradicts the estimate of 'frank_age_difference_hypothesis'
    label = "contradiction"
elif frank_age_difference_premise < frank_age_difference_hypothesis:
    # check if the age difference in the premise is less than 'frank_age_difference_hypothesis'
    label = "entailment"
else:
    # if the age difference in the premise does not contradict the 'frank_age_difference_hypothesis', we can infer neutrality
    label = "neutral"

print(label)
