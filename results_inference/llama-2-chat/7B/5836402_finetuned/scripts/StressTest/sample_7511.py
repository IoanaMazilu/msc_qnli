first_leg_duration_premise = 1
first_leg_speed_premise = 50
second_leg_duration_premise = 3
second_leg_speed_premise = 60

first_leg_duration_hypothesis = 7
first_leg_speed_hypothesis = 50
second_leg_duration_hypothesis = 3
second_leg_speed_hypothesis = 60

# the hypothesis refers to the duration and speed of the first and second legs of the trip mentioned in the premise
if first_leg_duration_premise!= first_leg_duration_hypothesis or \
   first_leg_speed_premise!= first_leg_speed_hypothesis or \
   second_leg_duration_premise!= second_leg_duration_hypothesis or \
   second_leg_speed_premise!= second_leg_speed_hypothesis:
    # check if any of the values in the hypothesis contradicts the values in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
