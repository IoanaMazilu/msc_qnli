home_beach_speed_premise = 80
home_beach_speed_hypothesis = 60
return_speed_premise = 70
return_speed_hypothesis = 70

# the hypothesis refers to the average speed of Carl's trip from home to the beach and back, which is also mentioned in the premise
if home_beach_speed_hypothesis!= home_beach_speed_premise:
    # check if the average speed of the trip from home to the beach in the hypothesis contradicts the average speed mentioned in the premise
    label = "contradiction"
elif return_speed_hypothesis!= return_speed_premise:
    # check if the average speed of the return trip from the beach to home in the hypothesis contradicts the average speed mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
