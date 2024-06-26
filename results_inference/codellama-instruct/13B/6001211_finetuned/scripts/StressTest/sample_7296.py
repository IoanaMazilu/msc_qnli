river_speed_premise = 2
river_speed_hypothesis = 1
row_time_premise = 1
row_time_hypothesis = 1

# the hypothesis refers to the river speed and rowing time mentioned in the premise
if river_speed_premise <= river_speed_hypothesis:
    # check if the estimate of 'river_speed_hypothesis' contradicts the river speed in the premise
    label = "contradiction"
elif row_time_hypothesis!= row_time_premise:
    # check if the rowing time in the hypothesis contradicts the rowing time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
