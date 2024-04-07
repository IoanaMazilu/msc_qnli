# Premise: Steve gets on the elevator at the 11 th floor of a building and rides up at a rate of 57 floors per minute.
# Hypothesis: Steve gets on the elevator at the less than 71 th floor of a building and rides up at a rate of 57 floors per minute.
# Golden Label: entailment

start_floor_premise = 11
start_floor_hypothesis = 71
rate_premise = 57
rate_hypothesis = 57

# the hypothesis refers to the floor Steve starts at and the rate he rides the elevator, both mentioned in the premise
if start_floor_hypothesis <= start_floor_premise:
    # check if the floor number in the hypothesis contradicts the start floor in the premise
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate of riding the elevator in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

