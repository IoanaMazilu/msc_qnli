distance_covered_premise = 800
distance_covered_hypothesis = 500
speed_sandy = 15

# the hypothesis refers to the distance Sandy covers, which is also mentioned in the premise
if distance_covered_hypothesis >= distance_covered_premise:
    # check if the distance in the hypothesis contradicts the premise (less than 800 meters)
    label = "contradiction"
elif distance_covered_hypothesis < distance_covered_premise:
    # the premise gives an estimate for the distance Sandy covers
    # a distance less than 'distance_covered_premise' does not contradict the premise
    # but the exact distance cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
