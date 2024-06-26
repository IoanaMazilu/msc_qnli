babysitting_age_premise = 20
babysitting_age_hypothesis = 40

# the hypothesis refers to the age Jane started babysitting, which is also mentioned in the premise
if babysitting_age_hypothesis!= babysitting_age_premise:
    # check if the age in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
else:
    # if the age in the hypothesis does not contradict the age mentioned in the premise, we can infer entailment
    label = "entailment"

print(label)
