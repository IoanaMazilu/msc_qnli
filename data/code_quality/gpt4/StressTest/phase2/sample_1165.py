travel_distance_premise = 7/2
travel_distance_hypothesis = 1/2

# the hypothesis specifies a precise distance Maria supposedly traveled before stopping, referenced also in the premise
if travel_distance_hypothesis >= travel_distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'travel_distance_premise'
    label = "contradiction"
elif travel_distance_hypothesis < travel_distance_premise:
    # if the hypothesis value doesn't contradict the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)
