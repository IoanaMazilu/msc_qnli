# Premise: At the same time, Albert gets on an elevator at the 51 st floor of the same building and rides down at the rate of 63 floors per minute.
# Hypothesis: At the same time, Albert gets on an elevator at the 81 st floor of the same building and rides down at the rate of 63 floors per minute.
# Golden Label: contradiction

start_floor_premise = 51
start_floor_hypothesis = 81
rate_premise = 63
rate_hypothesis = 63

# the hypothesis talks about Albert's starting floor and his rate of descent, both are also mentioned in the premise
if start_floor_hypothesis != start_floor_premise:
    # check if the starting floor in the hypothesis contradicts the starting floor in the premise
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate of descent in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

