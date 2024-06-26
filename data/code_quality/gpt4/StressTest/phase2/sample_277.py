travel_distance_premise = 660
travel_distance_hypothesis = 160

# the hypothesis talks about the distance Louisa traveled on the first day of her vacation, referenced also in the premise
if travel_distance_hypothesis >= travel_distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'travel_distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the travel distance
    # any travel distance less than 'travel_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
