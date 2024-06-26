premise_speed_home_to_beach = 40
premise_speed_home_to_beach_return = 70
hypothesis_speed_home_to_beach = 80
hypothesis_speed_home_to_beach_return = 70

# the hypothesis talks about the average speed of Carl's trip to the beach and back
if hypothesis_speed_home_to_beach <= premise_speed_home_to_beach:
    # check if the hypothesis value contradicts the estimate of more than 'premise_speed_home_to_beach'
    label = "contradiction"
elif hypothesis_speed_home_to_beach_return <= premise_speed_home_to_beach_return:
    # check if the hypothesis value contradicts the estimate of more than 'premise_speed_home_to_beach_return'
    label = "contradiction"
else:
    # the premise gives only estimates for the average speed of Carl's trip to the beach and back
    # any number of kilometers per hour greater than 'premise_speed_home_to_beach' and 'premise_speed_home_to_beach_return' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
