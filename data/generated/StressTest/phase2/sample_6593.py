# Premise: At the same time Joyce gets on an elevator on the 71 st floor of the same building and rides down at a rate of 93 floors per minute.
# Hypothesis: At the same time Joyce gets on an elevator on the 31 st floor of the same building and rides down at a rate of 93 floors per minute.
# Golden Label: contradiction

start_floor_premise = 71
start_floor_hypothesis = 31
rate_premise = 93
rate_hypothesis = 93

# the hypothesis refers to the same event of Joyce riding an elevator down, with details on the starting floor and the rate
if start_floor_hypothesis != start_floor_premise:
    # check if the starting floor in the hypothesis contradicts the starting floor in the premise
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

