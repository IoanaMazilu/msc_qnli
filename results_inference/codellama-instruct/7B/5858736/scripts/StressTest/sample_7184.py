passengers_ship_premise = 12
passengers_ship_hypothesis = 3

# the hypothesis talks about the number of passengers on a ship, referenced also in the premise
if passengers_ship_hypothesis <= passengers_ship_premise:
    # check if the hypothesis value contradicts the estimate of more than 'passengers_ship_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers
    # any number of passengers greater than 'passengers_ship_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
