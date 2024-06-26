premise = 5
hypothesis = 6

# the hypothesis refers to the number of people that can be seated on a bench
if hypothesis > premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people that can be seated on a bench
    # any number of people greater than 'premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
