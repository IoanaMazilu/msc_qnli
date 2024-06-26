total_journey_premise = 8800
total_journey_hypothesis = 1800

# the hypothesis refers to the total journey and the portion of the journey by air
if total_journey_hypothesis <= total_journey_premise:
    # check if the estimate of 'total_journey_hypothesis' contradicts the total journey in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total journey
    # any total journey greater than 'total_journey_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
