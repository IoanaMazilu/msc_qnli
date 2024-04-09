average_speed_premise_to_beach = 80
average_speed_premise_to_home = 70
average_speed_hypothesis_to_beach = 60
average_speed_hypothesis_to_home = 70

# the hypothesis refers to the average speeds of Carl's drives mentioned in the premise
if average_speed_premise_to_beach!= average_speed_hypothesis_to_beach:
    # check if the speed to the beach in the hypothesis contradicts the speed to the beach reported in the premise
    label = "contradiction"
elif average_speed_premise_to_home!= average_speed_hypothesis_to_home:
    # check if the speed home in the hypothesis contradicts the speed home reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
