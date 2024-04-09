passengers_premise = 3230000
passengers_hypothesis = 6979

# the hypothesis talks about the number of passengers using Kennedy Airport, referenced also in the premise
if passengers_hypothesis <= passengers_premise:
    # check if the hypothesis value contradicts the estimate of more than 'passengers_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers
    # any number of passengers greater than 'passengers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
