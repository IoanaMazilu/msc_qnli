total_journey_premise = 1800
total_journey_hypothesis = 7800

# the hypothesis refers to the total journey and the fraction of the total journey
if total_journey_hypothesis <= total_journey_premise:
    # check if the estimate of 'total_journey_hypothesis' contradicts the total journey in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total journey
    # any number of kilometres greater than 'total_journey_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)