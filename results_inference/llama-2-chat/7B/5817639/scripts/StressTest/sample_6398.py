passengers_premise = 1979
passengers_hypothesis = 6979

# the hypothesis talks about the number of airline passengers in a specific year, referenced also in the premise
if passengers_hypothesis <= passengers_premise:
    # check if the hypothesis value contradicts the estimate of 'passengers_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers
    # any number of passengers greater than 'passengers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
