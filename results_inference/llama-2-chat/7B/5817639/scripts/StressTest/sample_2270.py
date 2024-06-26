travel_speed_premise = 40
travel_speed_hypothesis = 80

# the hypothesis talks about the speed of Murali's journey, referenced also in the premise
if travel_speed_hypothesis >= travel_speed_premise:
    # check if the hypothesis value contradicts the estimate of the speed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of Murali's journey
    # any speed greater than 'travel_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
