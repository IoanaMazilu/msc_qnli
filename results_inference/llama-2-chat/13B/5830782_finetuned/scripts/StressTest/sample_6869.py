people_premise = 5
people_hypothesis = 5

# the hypothesis refers to the number of people that can be seated on a bench, mentioned in the premise
if people_hypothesis <= people_premise:
    # check if the hypothesis value contradicts the estimate of more than 'people_hypothesis'
    label = "contradiction"
else:
    # the premise gives an exact number of people
    # any number of people greater than 'people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
