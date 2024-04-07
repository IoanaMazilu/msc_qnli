# Premise: Stalin gets on the elevator at the 11 th floor of a building and rides up at a rate of 57 floors per minute.
# Hypothesis: Stalin gets on the elevator at the more than 11 th floor of a building and rides up at a rate of 57 floors per minute.
# Golden Label: contradiction

start_floor_premise = 11
start_floor_hypothesis = 11
rate_per_minute_premise = 57
rate_per_minute_hypothesis = 57

# the hypothesis talks about the floor where Stalin gets on the elevator and the rate of the elevator, both also mentioned in the premise
if start_floor_hypothesis != start_floor_premise:
    # check if the floor number in the hypothesis contradicts the floor number in the premise
    label = "contradiction"
elif rate_per_minute_hypothesis != rate_per_minute_premise:
    # check if the rate per minute in the hypothesis contradicts the rate per minute in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

