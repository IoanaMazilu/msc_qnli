babysitting_age_premise = 20
babysitting_age_hypothesis = 40

# the hypothesis refers to the age Jane started babysitting, which is also mentioned in the premise
if babysitting_age_premise >= babysitting_age_hypothesis:
    # check if the premise age contradicts the hypothesis age
    label = "contradiction"
else:
    # if the premise age does not contradict the hypothesis age, we can infer entailment
    label = "entailment"

print(label)
