premise_speed = 30
hypothesis_speed = 50

# the hypothesis refers to the speed of the car, which is mentioned in the premise
if premise_speed < hypothesis_speed:
    # check if the estimate of 'hypothesis_speed' contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the speed of the car
    # any speed greater than 'premise_speed' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
