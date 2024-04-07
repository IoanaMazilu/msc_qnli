# Premise: City A to city B, Andrew drove for 1 hr at 50 mph and for 3 hours at 60 mph.
# Hypothesis: City A to city B, Andrew drove for 4 hr at 50 mph and for 3 hours at 60 mph.
# Golden Label: contradiction

first_leg_time_premise = 1
first_leg_speed_premise = 50
second_leg_time_premise = 3
second_leg_speed_premise = 60

first_leg_time_hypothesis = 4
first_leg_speed_hypothesis = 50
second_leg_time_hypothesis = 3
second_leg_speed_hypothesis = 60

# the hypothesis refers to the driving times and speeds from city A to city B mentioned in the premise
if first_leg_time_hypothesis != first_leg_time_premise or first_leg_speed_hypothesis != first_leg_speed_premise:
    # check if the driving time or speed in the first leg of the journey in the hypothesis contradicts those reported in the premise
    label = "contradiction"
elif second_leg_time_hypothesis != second_leg_time_premise or second_leg_speed_hypothesis != second_leg_speed_premise:
    # check if the driving time or speed in the second leg of the journey in the hypothesis contradicts those reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

