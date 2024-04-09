traveled_distance_premise = 8/2
traveled_distance_hypothesis = 1/2

# the hypothesis refers to the distance Maria traveled before stopping, which is also mentioned in the premise
if traveled_distance_hypothesis >= traveled_distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'traveled_distance_premise'
    label = "contradiction"
elif traveled_distance_hypothesis < traveled_distance_premise:
    # if the hypothesis value is less than the premise value, it doesn't contradict the premise but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
