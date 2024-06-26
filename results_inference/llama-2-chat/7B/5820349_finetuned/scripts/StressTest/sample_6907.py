first_leg_time_premise = 2
first_leg_speed_premise = 44
second_leg_time_premise = 3
second_leg_speed_premise = 60

first_leg_time_hypothesis = 1
first_leg_speed_hypothesis = 44
second_leg_time_hypothesis = 3
second_leg_speed_hypothesis = 60

# the hypothesis refers to the driving times and speeds between city A and B mentioned in the premise
if first_leg_time_hypothesis >= first_leg_time_premise:
    # check if the estimate of 'first_leg_time_hypothesis' contradicts the estimate of less than 'first_leg_time_premise'
    label = "contradiction"
elif first_leg_speed_hypothesis!= first_leg_speed_premise or second_leg_time_hypothesis!= second_leg_time_premise or second_leg_speed_hypothesis!= second_leg_speed_premise:
    # check if the driving speeds or times in the hypothesis contradict the ones reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
