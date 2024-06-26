traveled_distance_premise = 3/2
traveled_distance_hypothesis = 1/2

# the hypothesis refers to the same car trip and the distance traveled by Maria mentioned in the premise
if traveled_distance_hypothesis >= traveled_distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'traveled_distance_premise'
    label = "contradiction"
elif traveled_distance_hypothesis < traveled_distance_premise:
    # the premise gives only an estimate for the distance traveled
    # any distance less than 'traveled_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
