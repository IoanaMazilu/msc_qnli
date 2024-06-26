babysitting_age_premise = 18
babysitting_age_hypothesis = 58

# the hypothesis refers to the age Jane started babysitting, which is also mentioned in the premise
if babysitting_age_premise!= babysitting_age_hypothesis:
    # check if the age in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis age does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
