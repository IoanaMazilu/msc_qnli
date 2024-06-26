floor_premise = 61
floor_hypothesis = 11
rate_floors_per_minute = 57

# the hypothesis talks about the floor David gets on the elevator and the rate of floors per minute, referenced also in the premise
if floor_hypothesis >= floor_premise:
    # check if the hypothesis value contradicts the estimate of less than 'floor_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the floor
    # any floor less than 'floor_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
