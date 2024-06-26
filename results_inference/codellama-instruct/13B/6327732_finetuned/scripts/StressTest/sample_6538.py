premise_speed = 50
hypothesis_speed = 30

# the hypothesis refers to the speed of the car mentioned in the premise
if hypothesis_speed >= premise_speed:
    # check if the hypothesis value contradicts the estimate of less than 'premise_speed'
    label = "contradiction"
else:
    # the premise gives an estimate for the speed of the car
    # any speed less than 'premise_speed' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
