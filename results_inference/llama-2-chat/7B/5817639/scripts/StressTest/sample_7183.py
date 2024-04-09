passenger_premise = 4/12
passenger_hypothesis = 1/12

# the hypothesis talks about the number of passengers on a ship, referenced also in the premise
if passenger_hypothesis <= passenger_premise:
    # check if the hypothesis value contradicts the estimate of less than 'passenger_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers
    # any number of passengers greater than 'passenger_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
