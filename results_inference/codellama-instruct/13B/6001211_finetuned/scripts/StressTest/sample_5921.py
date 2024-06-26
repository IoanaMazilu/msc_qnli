average_speed_to_beach_premise = 80
average_speed_to_beach_hypothesis = 80
average_speed_home_premise = 70
average_speed_home_hypothesis = 70

# the hypothesis refers to the average speeds of driving to the beach and back home, mentioned in the premise
if average_speed_to_beach_hypothesis <= average_speed_to_beach_premise:
    # check if the hypothesis value contradicts the premise value for the average speed to the beach
    label = "contradiction"
elif average_speed_home_hypothesis!= average_speed_home_premise:
    # check if the hypothesis value contradicts the premise value for the average speed home
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
