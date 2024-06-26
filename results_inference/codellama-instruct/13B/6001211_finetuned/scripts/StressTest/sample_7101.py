first_distance_premise = 240
first_speed_premise = 60
second_distance_premise = 120
second_speed_premise = 40

first_distance_hypothesis = 340
first_speed_hypothesis = 60
second_distance_hypothesis = 120
second_speed_hypothesis = 40

# the hypothesis refers to the distances and speeds mentioned in the premise
if first_distance_premise >= first_distance_hypothesis:
    # check if the estimate of 'first_distance_hypothesis' contradicts the distance driven at 60mph in the premise
    label = "contradiction"
elif first_speed_premise!= first_speed_hypothesis or second_distance_premise!= second_distance_hypothesis or second_speed_premise!= second_speed_hypothesis:
    # check if the speeds or distances in the hypothesis contradict the speeds or distances reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
