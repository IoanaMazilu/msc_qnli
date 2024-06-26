premise_speed_home_to_beach = 80
premise_speed_beach_to_home = 70
hypothesis_speed_home_to_beach = 60
hypothesis_speed_beach_to_home = 70

# the hypothesis refers to the speed of Carl's journey from his home to the beach and back home
if hypothesis_speed_home_to_beach < premise_speed_home_to_beach:
    # check if the hypothesis value contradicts the estimate of 'premise_speed_home_to_beach'
    label = "contradiction"
elif hypothesis_speed_beach_to_home!= premise_speed_beach_to_home:
    # check if the hypothesis value contradicts the estimate of 'premise_speed_beach_to_home'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
