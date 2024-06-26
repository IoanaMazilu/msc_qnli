average_speed_home_to_beach_premise = 40
average_speed_home_to_beach_hypothesis = 80
average_speed_return_premise = 70
average_speed_return_hypothesis = 70

# the hypothesis refers to the average speed of the trip to the beach and back, which are also mentioned in the premise
if average_speed_home_to_beach_hypothesis <= average_speed_home_to_beach_premise:
    # check if the hypothesis value contradicts the premise value for the average speed to the beach
    label = "contradiction"
elif average_speed_return_hypothesis!= average_speed_return_premise:
    # check if the hypothesis value contradicts the premise value for the average speed back from the beach
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
