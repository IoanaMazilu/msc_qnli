people_seated_premise = 2
people_seated_hypothesis = 5

# the hypothesis talks about the number of people seated on a bench, which is also referenced in the premise
if people_seated_hypothesis <= people_seated_premise:
    # check if the hypothesis value contradicts the estimate of more than 'people_seated_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people greater than 'people_seated_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
