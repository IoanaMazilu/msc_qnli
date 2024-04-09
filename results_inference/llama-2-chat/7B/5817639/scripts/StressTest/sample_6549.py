birds_flight_premise = 4
birds_flight_hypothesis = 7

# the hypothesis talks about the speed of birds flying simultaneously towards each other
if birds_flight_hypothesis <= birds_flight_premise:
    # check if the hypothesis value contradicts the estimate of less than 'birds_flight_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of birds flying simultaneously
    # any speed less than 'birds_flight_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
