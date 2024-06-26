travel_distance_premise = 8/2
travel_distance_hypothesis = 1/2

# the hypothesis talks about the distance traveled by Maria, referenced also in the premise
if travel_distance_hypothesis >= travel_distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'travel_distance_premise'
    label = "contradiction"
elif travel_distance_hypothesis == travel_distance_premise:
    # check if the distance traveled in the hypothesis is exactly the same as the distance traveled in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the travel distance
    # any travel distance less than 'travel_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
