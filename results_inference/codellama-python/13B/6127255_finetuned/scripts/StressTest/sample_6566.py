average_speed_to_beach_premise = 80
average_speed_to_beach_hypothesis = 60
average_speed_home_premise = 70
average_speed_home_hypothesis = 70

# the hypothesis refers to the average speeds of driving to the beach and home mentioned in the premise
if average_speed_to_beach_premise!= average_speed_to_beach_hypothesis:
    # check if the average speed to the beach in the hypothesis contradicts the average speed to the beach reported in the premise
    label = "contradiction"
elif average_speed_home_hypothesis!= average_speed_home_premise:
    # check if the average speed home in the hypothesis contradicts the average speed home reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
