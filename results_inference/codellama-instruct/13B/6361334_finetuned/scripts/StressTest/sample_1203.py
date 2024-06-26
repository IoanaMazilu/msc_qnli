average_speed_home_to_beach_premise = 80
average_speed_home_to_beach_hypothesis = 40
average_speed_return_home_premise = 70
average_speed_return_home_hypothesis = 70

# the hypothesis refers to the average speed of driving from home to the beach and returning home
if average_speed_home_to_beach_hypothesis <= average_speed_home_to_beach_premise:
    # check if the estimate of 'average_speed_home_to_beach_hypothesis' contradicts the average speed of driving from home to the beach in the premise
    label = "contradiction"
elif average_speed_return_home_hypothesis!= average_speed_return_home_premise:
    # check if the average speed of returning home in the hypothesis contradicts the average speed of returning home reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
