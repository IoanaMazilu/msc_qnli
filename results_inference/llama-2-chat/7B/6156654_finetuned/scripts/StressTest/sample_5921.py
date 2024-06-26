average_speed_home_to_beach_premise = 80
average_speed_home_to_beach_hypothesis = 80
average_speed_return_home_premise = 70
average_speed_return_home_hypothesis = 70

# the hypothesis refers to the same route and speeds as the premise
if average_speed_home_to_beach_hypothesis < average_speed_home_to_beach_premise:
    # check if the hypothesis speed is less than the speed in the premise
    label = "contradiction"
elif average_speed_return_home_hypothesis!= average_speed_return_home_premise:
    # check if the return speed in the hypothesis is different from the return speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
