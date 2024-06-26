average_speed_from_home_to_beach_premise = 80
average_speed_from_home_to_beach_hypothesis = 40
average_speed_return_home_premise = 70
average_speed_return_home_hypothesis = 70

# the hypothesis talks about the average speed of Carl's trip to the beach and back, which is also mentioned in the premise
if average_speed_from_home_to_beach_hypothesis > average_speed_from_home_to_beach_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif average_speed_return_home_hypothesis!= average_speed_return_home_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
