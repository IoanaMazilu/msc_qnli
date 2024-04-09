passenger_count_premise = float(1)/2 + 4*float(4) = 6
passenger_count_hypothesis = 3*float(2) + 4*float(4) = 14

# the hypothesis talks about the number of passengers at Logan Airport, referenced also in the premise
if passenger_count_hypothesis <= passenger_count_premise:
    # check if the hypothesis value contradicts the estimate of 'passenger_count_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers
    # any number of passengers greater than 'passenger_count_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
