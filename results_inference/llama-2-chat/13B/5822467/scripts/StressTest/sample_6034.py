people_own_premise = less_than_70
people_own_hypothesis = 40

# the hypothesis refers to the number of people owning cats, dogs, or rabbits in San Durango
if people_own_hypothesis <= people_own_premise:
    # check if the estimate of 'people_own_hypothesis' contradicts the number of people owning pets reported in the premise
    label = "contradiction"
elif people_own_hypothesis > people_own_premise:
    # the hypothesis value is greater than the premise value, so we can infer entailment
    label = "entailment"
else:
    # the premise only gives a lower bound for the number of people owning pets
    # any number of people owning pets less than or equal to 40 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
