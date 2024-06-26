premise_speed_home_to_beach = 80
premise_speed_beach_to_home = 70
hypothesis_speed_home_to_beach = 40

# the hypothesis refers to the speed of driving from home to the beach
if hypothesis_speed_home_to_beach <= premise_speed_home_to_beach:
    # check if the estimate of 'hypothesis_speed_home_to_beach' contradicts the speed of driving from home to the beach in the premise
    label = "contradiction"
elif premise_speed_beach_to_home!= hypothesis_speed_beach_to_home:
    # check if the speed of driving from the beach to home in the hypothesis contradicts the speed of driving from the beach to home in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
