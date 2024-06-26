premise_total_distance = 8 + 20 = 28
premise_average_speed = (8 + 20) / 2 = 14
premise_stop_time = 15

hypothesis_total_distance = 5
hypothesis_average_speed = 40
hypothesis_stop_time = 15

# the hypothesis talks about the total distance and average speed, referenced also in the premise
if hypothesis_total_distance <= premise_total_distance:
    # check if the hypothesis value contradicts the estimate of more than 'premise_total_distance'
    label = "contradiction"
elif hypothesis_average_speed <= premise_average_speed:
    # check if the hypothesis value contradicts the estimate of more than 'premise_average_speed'
    label = "contradiction"
elif hypothesis_stop_time!= premise_stop_time:
    # check if the number of minutes spent stopping in the hypothesis contradicts the number of minutes spent stopping reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
