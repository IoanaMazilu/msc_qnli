start_speed_premise = 10
start_speed_hypothesis = 90
increase_speed_premise = 20
increase_speed_hypothesis = 20

# the hypothesis talks about Xavier's initial speed and the speed increase pattern, referenced also in the premise
if start_speed_hypothesis <= start_speed_premise:
    # check if the hypothesis value contradicts the estimate of more than'start_speed_premise'
    label = "contradiction"
elif increase_speed_hypothesis!= increase_speed_premise:
    # check if the speed increase pattern in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the initial speed
    # any speed greater than'start_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
