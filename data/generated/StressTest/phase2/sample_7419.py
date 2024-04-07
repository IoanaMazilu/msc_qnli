# Premise: David gets on the elevator at the 11 th floor of a building and rides up at the rate of 57 floors per minute.
# Hypothesis: David gets on the elevator at the less than 61 th floor of a building and rides up at the rate of 57 floors per minute.
# Golden Label: entailment

start_floor_premise = 11
start_floor_hypothesis = 61
rate_premise = 57
rate_hypothesis = 57

# the hypothesis refers to the floor number where David gets on the elevator and the rate of riding up, both mentioned in the premise
if start_floor_hypothesis <= start_floor_premise:
    # check if the hypothesis value contradicts the premise's exact floor number
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate of riding up in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

