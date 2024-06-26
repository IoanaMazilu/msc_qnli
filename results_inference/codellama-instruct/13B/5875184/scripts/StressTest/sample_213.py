premise_speed = 36
hypothesis_speed = 76

# the hypothesis refers to the average speed of the whole journey
if premise_speed <= hypothesis_speed:
    # check if the estimate of 'hypothesis_speed' contradicts the average speed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speed
    # any speed greater than 'premise_speed' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
