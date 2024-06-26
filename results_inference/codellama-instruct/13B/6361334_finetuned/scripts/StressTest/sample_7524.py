passengers_premise = 6
passengers_hypothesis = 2

# the hypothesis refers to the number of passengers mentioned in the premise
if passengers_hypothesis <= passengers_premise:
    # check if the estimate of 'passengers_hypothesis' contradicts the number of passengers in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers
    # any number of passengers greater than 'passengers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
