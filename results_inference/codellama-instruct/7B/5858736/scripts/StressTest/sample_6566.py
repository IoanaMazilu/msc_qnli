premise_speed_home_to_beach = 80
premise_speed_home_to_beach_return = 70
hypothesis_speed_home_to_beach = 60
hypothesis_speed_home_to_beach_return = 70

# the hypothesis talks about the average speed of Carl's trip to the beach and back
if hypothesis_speed_home_to_beach <= premise_speed_home_to_beach and hypothesis_speed_home_to_beach_return <= premise_speed_home_to_beach_return:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speed of Carl's trip to the beach and back
    # any average speed greater than 'premise_speed_home_to_beach' and 'premise_speed_home_to_beach_return' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
