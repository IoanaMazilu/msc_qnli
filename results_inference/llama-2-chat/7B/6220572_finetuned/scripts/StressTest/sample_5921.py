speed_premise = 80
speed_hypothesis = 80
speed_return_premise = 70
speed_return_hypothesis = 70

# the hypothesis refers to the average speed of the trip mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis estimate contradicts the speed reported in the premise
    label = "contradiction"
elif speed_return_hypothesis!= speed_return_premise:
    # check if the return speed in the hypothesis contradicts the return speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
