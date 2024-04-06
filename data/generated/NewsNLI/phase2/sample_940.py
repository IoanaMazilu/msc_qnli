# Premise: Thompson sought to break 392 mph to set the record for his vehicle class and hoped to be the first to drive a piston engine car 450 mph.
# Hypothesis: He has come within 20 mph of record for all piston engine cars.
# Golden Label: neutral

record_goal_premise = 392
piston_engine_car_goal_premise = 450
near_record_hypothesis = 20

# the hypothesis mentions how close Thompson came to the record for all piston engine cars
# the premise talks about the specific goals Thompson had for his vehicle class and for all piston engine cars
# the hypothesis does not specify if the record mentioned refers to his vehicle class or all piston engine cars
if near_record_hypothesis >= piston_engine_car_goal_premise - record_goal_premise:
    # check if the difference in speed from the hypothesis contradicts the difference in speed in the premise
    label = "contradiction"
else:
    # if the speed difference from the hypothesis does not contradict the speed difference in the premise, we can infer neutrality
    label = "neutral"

print(label)

