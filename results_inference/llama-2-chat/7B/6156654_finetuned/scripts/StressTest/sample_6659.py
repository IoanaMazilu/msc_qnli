karen_speed_premise = 60
tom_speed_premise = 45
karen_speed_hypothesis = 70
tom_speed_hypothesis = 45

# the hypothesis refers to the average speed of Karen and Tom, which are also mentioned in the premise
if karen_speed_premise!= karen_speed_hypothesis:
    # check if the average speed of Karen in the hypothesis contradicts the average speed of Karen in the premise
    label = "contradiction"
elif tom_speed_premise!= tom_speed_hypothesis:
    # check if the average speed of Tom in the hypothesis contradicts the average speed of Tom in the premise
    label = "contradiction"
else:
    # if the average speed of Karen and Tom in the hypothesis do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
