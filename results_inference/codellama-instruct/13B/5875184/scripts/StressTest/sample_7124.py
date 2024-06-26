premise_speed = 4
hypothesis_speed = 8

# the hypothesis refers to the speed of jogging and walking
if hypothesis_speed < premise_speed:
    # check if the estimate of 'hypothesis_speed' contradicts the speed of jogging in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of jogging
    # any speed of jogging less than 'premise_speed' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
