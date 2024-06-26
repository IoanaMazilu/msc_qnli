babysitting_age_premise = 20
babysitting_age_hypothesis = 40

# the hypothesis refers to the age Jane started babysitting, which is also mentioned in the premise
if babysitting_age_premise >= babysitting_age_hypothesis:
    # check if the age in the premise contradicts the estimate of less than 'babysitting_age_hypothesis'
    label = "contradiction"
else:
    # if the premise age does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
