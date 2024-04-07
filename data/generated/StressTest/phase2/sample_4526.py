# Premise: A train travels from Albany to Syracuse, a distance of 120 miles, at the average rate of 30 miles per hour.
# Hypothesis: A train travels from Albany to Syracuse, a distance of 520 miles, at the average rate of 30 miles per hour.
# Golden Label: contradiction

distance_premise = 120
distance_hypothesis = 520
rate_premise = 30
rate_hypothesis = 30

# the hypothesis refers to the distance and rate of travel mentioned in the premise
if distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate of travel in the hypothesis contradicts the rate of travel reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

