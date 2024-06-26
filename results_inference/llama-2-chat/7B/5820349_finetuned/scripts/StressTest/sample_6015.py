babysitting_start_age_premise = 20
babysitting_start_age_hypothesis = 40

# the hypothesis refers to the age Jane started babysitting, which is also mentioned in the premise
if babysitting_start_age_premise >= babysitting_start_age_hypothesis:
    # check if the age in the premise contradicts the hypothesis that Jane started babysitting less than 'babysitting_start_age_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
