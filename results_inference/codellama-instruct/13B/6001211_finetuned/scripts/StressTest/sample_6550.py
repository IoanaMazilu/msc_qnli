first_bird_speed_premise = 7
first_bird_speed_hypothesis = 4
second_bird_speed_premise = 1
second_bird_speed_hypothesis = 1

# the hypothesis refers to the speed of the two birds mentioned in the premise
if first_bird_speed_hypothesis >= first_bird_speed_premise:
    # check if the speed of the first bird in the hypothesis contradicts the speed of the first bird in the premise
    label = "contradiction"
elif second_bird_speed_hypothesis!= second_bird_speed_premise:
    # check if the speed of the second bird in the hypothesis contradicts the speed of the second bird in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of the first bird
    # any speed less than 'first_bird_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
