babysitting_age_premise = 18
babysitting_age_hypothesis = 58

# the hypothesis refers to the age Jane started babysitting, as mentioned in the premise
if babysitting_age_premise > babysitting_age_hypothesis:
    # check if the premise contradicts the hypothesis' claim of Jane starting babysitting at less than 'babysitting_age_hypothesis'
    label = "contradiction"
else:
    # the premise fully supports that Jane started babysitting at an age less than 'babysitting_age_hypothesis'
    label = "entailment"

print(label)
