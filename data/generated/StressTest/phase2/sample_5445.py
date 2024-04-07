# Premise: A train travels from Albany to Syracuse, a distance of 100 miles, at the average rate of 50 miles per hour.
# Hypothesis: A train travels from Albany to Syracuse, a distance of less than 700 miles, at the average rate of 50 miles per hour.
# Golden Label: entailment

distance_premise = 100
distance_hypothesis = 700
rate_premise = 50
rate_hypothesis = 50

# the hypothesis refers to the distance and rate of travel mentioned in the premise
if distance_hypothesis < distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate of travel in the hypothesis contradicts the rate of travel reported in the premise
    label = "contradiction"
elif distance_hypothesis > distance_premise:
    # the premise gives only an exact distance
    # any distance less than 'distance_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

