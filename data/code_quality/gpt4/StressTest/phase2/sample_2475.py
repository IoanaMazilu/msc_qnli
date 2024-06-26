avg_speed_first_part_premise = 15
avg_speed_first_part_hypothesis = 75
avg_speed_second_part_premise = 30
avg_speed_second_part_hypothesis = 30

# the hypothesis refers to the average speeds driven by Gwen in the first and second part of her trip, as mentioned in the premise
if avg_speed_first_part_hypothesis <= avg_speed_first_part_premise:
    # check if the estimate of 'avg_speed_first_part_hypothesis' contradicts the average speed in the first part of the trip reported in the premise
    label = "contradiction"
elif avg_speed_second_part_hypothesis != avg_speed_second_part_premise:
    # check if the average speed in the second part of the trip in the hypothesis contradicts the average speed in the second part of the trip reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
