speed_premise = 40
speed_hypothesis = 10

# the hypothesis refers to the speed of Bob's car, which is mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the estimate of'speed_hypothesis' contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of Bob's car
    # any speed greater than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
