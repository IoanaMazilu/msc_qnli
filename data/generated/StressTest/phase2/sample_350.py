# Premise: At the same time Joyce gets on an elevator on the 51 st floor of the same building and rides down at a rate of 53 floors per minute.
# Hypothesis: At the same time Joyce gets on an elevator on the 81 st floor of the same building and rides down at a rate of 53 floors per minute.
# Golden Label: contradiction

start_floor_premise = 51
start_floor_hypothesis = 81
rate_premise = 53
rate_hypothesis = 53

# the hypothesis refers to the initial floor and the rate of descent of an elevator mentioned in the premise
if start_floor_hypothesis != start_floor_premise:
    # check if the starting floor in the hypothesis contradicts the starting floor reported in the premise
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate of descent in the hypothesis contradicts the rate of descent reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
