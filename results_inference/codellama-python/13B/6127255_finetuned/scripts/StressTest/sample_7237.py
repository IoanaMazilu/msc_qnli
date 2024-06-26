travel_distance_premise = 440
travel_distance_hypothesis = 240

# the hypothesis talks about the distance traveled by Louisa on the first day of her vacation, which is also mentioned in the premise
if travel_distance_hypothesis >= travel_distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'travel_distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the travel distance
    # any travel distance less than 'travel_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
