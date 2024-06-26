average_speed_premise = 40
average_speed_hypothesis = 80
return_speed_premise = 70
return_speed_hypothesis = 70

# the hypothesis talks about the average speed of Carl's trip to the beach and back, which is also mentioned in the premise
if average_speed_hypothesis <= average_speed_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif return_speed_hypothesis!= return_speed_premise:
    # check if the return speed in the hypothesis contradicts the return speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and the premise values do not contradict each other, we can infer entailment
    label = "entailment"

print(label)
