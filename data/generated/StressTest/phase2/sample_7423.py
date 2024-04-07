# Premise: At the same time, Albert gets on an elevator at the less than 61 st floor of the same building and rides down at the rate of 63 floors per minute.
# Hypothesis: At the same time, Albert gets on an elevator at the 51 st floor of the same building and rides down at the rate of 63 floors per minute.
# Golden Label: neutral

elevator_floor_premise = 61
elevator_floor_hypothesis = 51
elevator_speed_premise = 63
elevator_speed_hypothesis = 63

# the hypothesis refers to the floor number and speed of Albert's elevator ride mentioned in the premise
if elevator_floor_hypothesis >= elevator_floor_premise:
    # check if the floor number 'elevator_floor_hypothesis' contradicts the estimate of less than 'elevator_floor_premise' floors
    label = "contradiction"
elif elevator_speed_hypothesis != elevator_speed_premise:
    # check if the speed of the ride in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the values in the hypothesis do not contradict the values from the premise, we can infer entailment
    label = "entailment"

print(label)

