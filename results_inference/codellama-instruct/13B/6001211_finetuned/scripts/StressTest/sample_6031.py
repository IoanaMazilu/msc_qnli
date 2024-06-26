travel_distance_premise = 8/2
travel_distance_hypothesis = 1/2

# the hypothesis refers to the distance Maria traveled during a car trip, also mentioned in the premise
if travel_distance_hypothesis >= travel_distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'travel_distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance Maria traveled
    # any distance less than 'travel_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
