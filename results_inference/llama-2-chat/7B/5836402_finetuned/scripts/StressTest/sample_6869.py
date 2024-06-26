people_premise = 5
people_hypothesis = 5

# the hypothesis refers to the number of people mentioned in the premise
if people_hypothesis <= people_premise:
    # check if the hypothesis value contradicts the estimate of 'people_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people greater than 'people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
