# Premise: Steve gets on the elevator at the less than 81 th floor of a building and rides up at a rate of 47 floors per minute.
# Hypothesis: Steve gets on the elevator at the 11 th floor of a building and rides up at a rate of 47 floors per minute.
# Golden Label: neutral

elevator_floor_premise = 81
elevator_floor_hypothesis = 11
elevator_rate_premise = 47
elevator_rate_hypothesis = 47

# the hypothesis refers to the floor and the rate at which Steve rides the elevator, both mentioned in the premise
if elevator_floor_hypothesis >= elevator_floor_premise:
    # check if the floor in the hypothesis contradicts the estimate of 'less than elevator_floor_premise' floors
    label = "contradiction"
elif elevator_rate_hypothesis != elevator_rate_premise:
    # check if the rate in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

