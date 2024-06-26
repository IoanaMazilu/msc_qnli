average_speed_to_beach_premise = 80
average_speed_to_beach_hypothesis = 80
average_speed_home_premise = 70
average_speed_home_hypothesis = 70

# the hypothesis refers to the average speeds of Carl's trips mentioned in the premise
if average_speed_to_beach_hypothesis <= average_speed_to_beach_premise:
    # check if the estimate of 'average_speed_to_beach_hypothesis' contradicts the average speed to the beach in the premise
    label = "contradiction"
elif average_speed_home_hypothesis!= average_speed_home_premise:
    # check if the average speed home in the hypothesis contradicts the average speed home reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
