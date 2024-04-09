approximate_passengers_premise = 1979
approximate_passengers_hypothesis = 7979

# the hypothesis refers to the number of passengers in a different year than the premise
if approximate_passengers_hypothesis <= approximate_passengers_premise:
    # check if the estimate of 'approximate_passengers_hypothesis' contradicts the number of passengers in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers in a specific year
    # any number of passengers greater than 'approximate_passengers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
