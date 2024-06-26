passengers_premise = 32300000
passengers_hypothesis = 32300000

# the hypothesis refers to the number of passengers traveling to or from the United States mentioned in the premise
if passengers_hypothesis <= passengers_premise:
    # check if the estimate of 'passengers_hypothesis' contradicts the number of passengers in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers, and the hypothesis value is consistent with it
    label = "neutral"

print(label)
