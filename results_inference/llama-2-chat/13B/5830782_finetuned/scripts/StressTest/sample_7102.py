first_distance_premise = 340
first_distance_hypothesis = 240
second_distance_premise = 120
second_distance_hypothesis = 120
speed_first_part_premise = 60
speed_first_part_hypothesis = 60
speed_second_part_premise = 40
speed_second_part_hypothesis = 40

# the hypothesis refers to the distances and speeds of Joe's driving, mentioned in the premise
if first_distance_hypothesis >= first_distance_premise:
    # check if the distance in the first part of the drive in the hypothesis contradicts the premise
    label = "contradiction"
elif second_distance_hypothesis!= second_distance_premise:
    # check if the distance in the second part of the drive in the hypothesis contradicts the premise
    label = "contradiction"
elif speed_first_part_hypothesis!= speed_first_part_premise:
    # check if the speed in the first part of the drive in the hypothesis contradicts the premise
    label = "contradiction"
elif speed_second_part_hypothesis!= speed_second_part_premise:
    # check if the speed in the second part of the drive in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
