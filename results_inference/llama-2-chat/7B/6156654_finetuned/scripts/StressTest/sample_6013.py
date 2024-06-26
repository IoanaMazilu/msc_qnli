karen_speed_premise = 20
tom_speed_premise = 45
karen_speed_hypothesis = 60
tom_speed_hypothesis = 45

# the hypothesis talks about the speed of Karen and Tom, which are also mentioned in the premise
if karen_speed_premise > karen_speed_hypothesis:
    # check if the average speed of Karen in the hypothesis contradicts the average speed of Karen in the premise
    label = "contradiction"
elif tom_speed_hypothesis!= tom_speed_premise:
    # check if the average speed of Tom in the hypothesis contradicts the average speed of Tom in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
