birds_flight_premise = 4
birds_flight_hypothesis = 3

# the hypothesis talks about the speed of the birds, which is also mentioned in the premise
if birds_flight_hypothesis <= birds_flight_premise:
    # check if the hypothesis value contradicts the estimate of the speed of the first bird in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of the first bird
    # any speed greater than 'birds_flight_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
