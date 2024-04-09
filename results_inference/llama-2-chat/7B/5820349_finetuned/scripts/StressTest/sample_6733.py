start_road_premise = 3
start_road_hypothesis = 2

# the hypothesis refers to the starting point of Bill's walk mentioned in the premise
if start_road_hypothesis >= start_road_premise:
    # check if the starting point in the hypothesis contradicts the estimate of less than'start_road_premise'
    label = "contradiction"
elif start_road_hypothesis < start_road_premise:
    # the premise gives only an estimate for the starting point
    # any starting point less than'start_road_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
