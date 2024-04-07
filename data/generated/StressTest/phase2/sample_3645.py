# Premise: A train travels from Albany to Syracuse, a distance of 120 miles, at the average rate of 40 miles per hour.
# Hypothesis: A train travels from Albany to Syracuse, a distance of less than 820 miles, at the average rate of 40 miles per hour.
# Golden Label: entailment

distance_premise = 120
distance_hypothesis = 820
rate_premise = 40
rate_hypothesis = 40

# the hypothesis mentions the distance and rate of the train travel, also referred in the premise
if distance_hypothesis < distance_premise:
    # check if the distance in the hypothesis contradicts the distance mentioned in the premise
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate of travel in the hypothesis contradicts the rate of travel mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

