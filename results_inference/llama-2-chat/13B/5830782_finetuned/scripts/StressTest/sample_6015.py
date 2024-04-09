babysitting_age_premise = 20
babysitting_age_hypothesis = 40

# the hypothesis refers to the age Jane started babysitting, which is also mentioned in the premise
if babysitting_age_premise > babysitting_age_hypothesis:
    # check if the age Jane started babysitting in the premise contradicts the age in the hypothesis
    label = "contradiction"
elif babysitting_age_premise < babysitting_age_hypothesis:
    # if the premise age is less than the age in the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if the premise age is equal to the age in the hypothesis, it is neutral as it doesn't explicitly entail or contradict
    label = "neutral"

print(label)
