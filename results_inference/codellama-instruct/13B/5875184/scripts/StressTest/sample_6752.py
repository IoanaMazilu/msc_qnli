premise = 50
hypothesis = 50

# the hypothesis refers to the number of people in the city who own cats, dogs, or rabbits
if hypothesis > premise:
    # check if the hypothesis value contradicts the estimate of more than 'premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who own cats, dogs, or rabbits
    # any number of people greater than 'premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
