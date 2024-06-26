distance_premise = 820
distance_hypothesis = 120
rate_premise = 40
rate_hypothesis = 40

# The hypothesis refers to the distance and rate of train travel mentioned in the premise
if distance_hypothesis >= distance_premise:
    # Check if the distance in the hypothesis contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif rate_hypothesis != rate_premise:
    # Check if the travel rate in the hypothesis contradicts the travel rate mentioned in the premise
    label = "contradiction"
else:
    # The premise gives only an estimate for the distance
    # Any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
