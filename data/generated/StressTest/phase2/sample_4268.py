# Premise: city A to city B, Andrew drove for 1 hour at 50 mph and for 3 hours at 60 mph.
# Hypothesis: city A to city B, Andrew drove for 5 hour at 50 mph and for 3 hours at 60 mph.
# Golden Label: contradiction

# driving time and speed from city A to city B
first_leg_time_premise = 1
first_leg_speed_premise = 50
second_leg_time_premise = 3
second_leg_speed_premise = 60

first_leg_time_hypothesis = 5
first_leg_speed_hypothesis = 50
second_leg_time_hypothesis = 3
second_leg_speed_hypothesis = 60

# the hypothesis refers to the driving time and speed from city A to city B mentioned in the premise
if first_leg_time_premise != first_leg_time_hypothesis:
    # check if the driving time in the first leg in the hypothesis contradicts the driving time in the first leg reported in the premise
    label = "contradiction"
elif second_leg_time_premise != second_leg_time_hypothesis:
    # check if the driving time in the second leg in the hypothesis contradicts the driving time in the second leg reported in the premise
    label = "contradiction"
elif first_leg_speed_premise != first_leg_speed_hypothesis:
    # check if the driving speed in the first leg in the hypothesis contradicts the driving speed in the first leg reported in the premise
    label = "contradiction"
elif second_leg_speed_premise != second_leg_speed_hypothesis:
    # check if the driving speed in the second leg in the hypothesis contradicts the driving speed in the second leg reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

