passenger_count_premise = 42
passenger_count_hypothesis = 42

# the hypothesis talks about the number of passengers on a ship, referenced also in the premise
if passenger_count_hypothesis <= passenger_count_premise:
    # check if the hypothesis value contradicts the estimate of 'passenger_count_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers
    # any number of passengers greater than 'passenger_count_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
