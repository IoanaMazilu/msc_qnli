first_part_speed_premise = 30
first_part_speed_hypothesis = 30
second_part_speed_premise = 15
second_part_speed_hypothesis = 15

# the hypothesis talks about the speed of Susan's trip, which is also mentioned in the premise
if first_part_speed_hypothesis >= first_part_speed_premise:
    # check if the hypothesis speed contradicts the premise speed for the first part of the trip
    label = "contradiction"
elif second_part_speed_hypothesis != second_part_speed_premise:
    # check if the speed for the second part of the trip in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
