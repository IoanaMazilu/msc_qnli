average_speed_premise = 40
average_speed_hypothesis = 80
average_speed_return_premise = 70
average_speed_return_hypothesis = 70

# the hypothesis refers to the average speed of the drive mentioned in the premise
if average_speed_hypothesis <= average_speed_premise:
    # check if the hypothesis value contradicts the average speed reported in the premise
    label = "contradiction"
elif average_speed_return_hypothesis!= average_speed_return_premise:
    # check if the return speed in the hypothesis contradicts the return speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
