# Premise: Steve gets on the elevator at the 11 th floor of a building and rides up at a rate of 47 floors per minute.
# Hypothesis: Steve gets on the elevator at the more than 11 th floor of a building and rides up at a rate of 47 floors per minute.
# Golden Label: contradiction

start_floor_premise = 11
start_floor_hypothesis = 11
rate_premise = 47
rate_hypothesis = 47

# the hypothesis talks about the floor where Steve gets on the elevator and the ride rate, both mentioned in the premise
if start_floor_hypothesis != start_floor_premise:
    # check if the floor number in the hypothesis contradicts the floor number mentioned in the premise
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the ride rate in the hypothesis contradicts the ride rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

