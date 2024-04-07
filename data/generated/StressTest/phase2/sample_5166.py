# Premise: A train travels from Albany to Syracuse, a distance of 120 miles, at the average rate of 50 miles per hour.
# Hypothesis: A train travels from Albany to Syracuse, a distance of less than 520 miles, at the average rate of 50 miles per hour.
# Golden Label: entailment

distance_premise = 120
distance_hypothesis = 520
avg_rate_premise = 50
avg_rate_hypothesis = 50

# the hypothesis refers to the same train travel from Albany to Syracuse as in the premise
if distance_premise > distance_hypothesis:
    # check if the distance from the premise contradicts the distance in the hypothesis
    label = "contradiction"
elif avg_rate_premise != avg_rate_hypothesis:
    # check if the average rate in the hypothesis contradicts the average rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

