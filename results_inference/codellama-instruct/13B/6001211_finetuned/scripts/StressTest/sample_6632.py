distance_covered_premise = 500
distance_covered_hypothesis = 500
speed_sandy = 15

# the hypothesis refers to the distance covered by Sandy, also mentioned in the premise
if distance_covered_hypothesis <= distance_covered_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives the exact distance covered by Sandy
    # any distance greater than 'distance_covered_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
