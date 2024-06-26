first_bird_speed_premise = 4
second_bird_speed_premise = 1
first_bird_speed_hypothesis = 3
second_bird_speed_hypothesis = 1

# the hypothesis refers to the speed of the two birds mentioned in the premise
if first_bird_speed_premise!= first_bird_speed_hypothesis:
    # check if the speed of the first bird in the hypothesis contradicts the speed of the first bird in the premise
    label = "contradiction"
elif second_bird_speed_premise!= second_bird_speed_hypothesis:
    # check if the speed of the second bird in the hypothesis contradicts the speed of the second bird in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
