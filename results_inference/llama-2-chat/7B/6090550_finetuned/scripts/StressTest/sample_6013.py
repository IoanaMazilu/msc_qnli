karen_speed_premise = 20
karen_speed_hypothesis = 60
tom_speed_premise = 45
tom_speed_hypothesis = 45

# the hypothesis refers to the average speed of Karen and Tom mentioned in the premise
if karen_speed_premise <= karen_speed_hypothesis:
    # check if the average speed of Karen in the hypothesis contradicts the premise
    label = "contradiction"
elif tom_speed_hypothesis!= tom_speed_premise:
    # check if the average speed of Tom in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)