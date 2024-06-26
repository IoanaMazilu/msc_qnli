karen_speed_premise = 60
tom_speed_premise = 45
karen_speed_hypothesis = 20
tom_speed_hypothesis = 45

# the hypothesis refers to the driving speeds of Karen and Tom mentioned in the premise
if karen_speed_premise!= karen_speed_hypothesis:
    # check if the speed of Karen in the hypothesis contradicts the speed of Karen reported in the premise
    label = "contradiction"
elif tom_speed_hypothesis!= tom_speed_premise:
    # check if the speed of Tom in the hypothesis contradicts the speed of Tom reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
