average_speed_home_to_beach_premise = 40
average_speed_beach_to_home_premise = 70
average_speed_home_to_beach_hypothesis = 80
average_speed_beach_to_home_hypothesis = 70

# the hypothesis refers to the average speed of Carl's drive from home to the beach and back, mentioned in the premise
if average_speed_home_to_beach_hypothesis <= average_speed_home_to_beach_premise:
    # check if the average speed to the beach in the hypothesis contradicts the premise
    label = "contradiction"
elif average_speed_beach_to_home_hypothesis!= average_speed_beach_to_home_premise:
    # check if the average speed from the beach to home in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
