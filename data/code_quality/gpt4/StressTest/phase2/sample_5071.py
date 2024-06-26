initial_speed_premise = 40
initial_speed_hypothesis = 90
speed_increase_interval = 12
speed_increase_amount = 10

# the hypothesis talks about Xavier's initial and increased speed, referenced also in the premise
if initial_speed_hypothesis <= initial_speed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'initial_speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the initial speed
    # any initial speed greater than 'initial_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
