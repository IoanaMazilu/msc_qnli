premise_speed = 30
hypothesis_speed = 10

# the hypothesis refers to the speed of the car mentioned in the premise
if hypothesis_speed >= premise_speed:
    # check if the estimate of 'hypothesis_speed' contradicts the speed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed less than 'premise_speed' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
