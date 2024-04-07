# Premise: David gets on the elevator at the 11 th floor of a building and rides up at the rate of 57 floors per minute.
# Hypothesis: David gets on the elevator at the 81 th floor of a building and rides up at the rate of 57 floors per minute.
# Golden Label: contradiction

start_floor_premise = 11
start_floor_hypothesis = 81
rate_premise = 57
rate_hypothesis = 57

# the hypothesis talks about the start floor and ride rate which are mentioned in the premise
if start_floor_hypothesis != start_floor_premise:
    # check if the start floor in the hypothesis contradicts the start floor in the premise
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the ride rate in the hypothesis contradicts the ride rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

