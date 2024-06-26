average_speed_home_to_beach_premise = 40
average_speed_beach_to_home_premise = 70
average_speed_home_to_beach_hypothesis = 80
average_speed_beach_to_home_hypothesis = 70

# the hypothesis talks about the average speed of the journey from home to the beach and back, which are also mentioned in the premise
if average_speed_home_to_beach_hypothesis <= average_speed_home_to_beach_premise:
    # check if the hypothesis value for the average speed of the journey from home to the beach contradicts the premise
    label = "contradiction"
elif average_speed_beach_to_home_hypothesis!= average_speed_beach_to_home_premise:
    # check if the hypothesis value for the average speed of the journey from the beach to home contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
