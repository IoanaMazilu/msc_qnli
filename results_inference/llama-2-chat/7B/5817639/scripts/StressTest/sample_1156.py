passenger_premise = 3730000
passenger_hypothesis = 1330000

# the hypothesis talks about the number of airline passengers using Kennedy Airport in 1979
if passenger_hypothesis <= passenger_premise:
    # check if the hypothesis value contradicts the estimate of 'passenger_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers, but the hypothesis value is consistent with it
    label = "neutral"

print(label)
