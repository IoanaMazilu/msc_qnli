average_speed_premise_from_beach = 80
average_speed_premise_from_home = 70
average_speed_hypothesis_from_beach = 60
average_speed_hypothesis_from_home = 70

# the hypothesis talks about the average speed from the beach and home, referenced also in the premise
if average_speed_hypothesis_from_beach!= average_speed_premise_from_beach:
    # check if the average speed from the beach in the hypothesis contradicts the average speed from the beach in the premise
    label = "contradiction"
elif average_speed_hypothesis_from_home!= average_speed_premise_from_home:
    # check if the average speed from home in the hypothesis contradicts the average speed from home in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
