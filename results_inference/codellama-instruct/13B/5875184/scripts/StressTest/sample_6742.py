premise_speed = 20
hypothesis_speed = 30

# the hypothesis refers to the speed mentioned in the premise
if hypothesis_speed <= premise_speed:
    # check if the estimate of 'hypothesis_speed' contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed greater than 'premise_speed' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
