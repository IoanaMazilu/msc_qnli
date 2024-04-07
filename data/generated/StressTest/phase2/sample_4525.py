# Premise: A train travels from Albany to Syracuse, a distance of less than 620 miles, at the average rate of 30 miles per hour.
# Hypothesis: A train travels from Albany to Syracuse, a distance of 120 miles, at the average rate of 30 miles per hour.
# Golden Label: neutral

distance_premise = 620
distance_hypothesis = 120
rate_premise = 30
rate_hypothesis = 30

# the hypothesis refers to the distance and rate mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # check if the rate in the hypothesis contradicts the rate reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

