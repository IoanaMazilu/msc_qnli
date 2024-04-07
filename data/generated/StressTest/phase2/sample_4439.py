# Premise: Steve gets on the elevator at the 11 th floor of a building and rides up at a rate of 72 floors per minute.
# Hypothesis: Steve gets on the elevator at the 21 th floor of a building and rides up at a rate of 72 floors per minute.
# Golden Label: contradiction

start_floor_premise = 11
start_floor_hypothesis = 21
rate_premise = 72
rate_hypothesis = 72

# the hypothesis talks about the starting floor and the rate of elevator ride, both mentioned in the premise
if start_floor_hypothesis != start_floor_premise:
    # check if the starting floor in the hypothesis contradicts the starting floor in the premise
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate of ride in the hypothesis contradicts the rate of ride in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

