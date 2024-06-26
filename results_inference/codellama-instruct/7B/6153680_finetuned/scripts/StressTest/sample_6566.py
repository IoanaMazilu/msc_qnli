average_speed_to_beach_premise = 80
average_speed_to_beach_hypothesis = 60
average_speed_return_premise = 70
average_speed_return_hypothesis = 70

# the hypothesis talks about the average speed of Carl's trip to the beach and back, which is also mentioned in the premise
if average_speed_to_beach_hypothesis!= average_speed_to_beach_premise:
    # check if the average speed to the beach in the hypothesis contradicts the average speed to the beach in the premise
    label = "contradiction"
elif average_speed_return_hypothesis!= average_speed_return_premise:
    # check if the average speed back to the beach in the hypothesis contradicts the average speed back to the beach in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
