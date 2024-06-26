passengers_premise = 12
passengers_hypothesis = 7

# the hypothesis refers to the number of passengers on a ship, which is also mentioned in the premise
if passengers_hypothesis >= passengers_premise:
    # check if the hypothesis value contradicts the number of passengers in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers
    # any number of passengers less than 'passengers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)