average_speed_premise = 40
average_speed_hypothesis = 80
return_speed_premise = 70
return_speed_hypothesis = 70

# the hypothesis talks about the average speeds of Carl's trips, referenced also in the premise
if average_speed_hypothesis <= average_speed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'average_speed_premise'
    label = "contradiction"
elif return_speed_hypothesis!= return_speed_premise:
    # check if the return speed in the hypothesis contradicts the return speed reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speed
    # any average speed greater than 'average_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
