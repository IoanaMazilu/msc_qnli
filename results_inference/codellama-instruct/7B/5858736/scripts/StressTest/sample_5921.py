premise_speed_home_to_beach = 80
premise_speed_home_to_beach_return = 70
hypothesis_speed_home_to_beach = 80
hypothesis_speed_home_to_beach_return = 70

# the hypothesis talks about the average speed of Carl's trip to the beach and back
if hypothesis_speed_home_to_beach <= premise_speed_home_to_beach:
    # check if the hypothesis value contradicts the estimate of more than 'premise_speed_home_to_beach'
    label = "contradiction"
elif hypothesis_speed_home_to_beach_return!= premise_speed_home_to_beach_return:
    # check if the hypothesis value contradicts the estimate of 'premise_speed_home_to_beach_return'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
