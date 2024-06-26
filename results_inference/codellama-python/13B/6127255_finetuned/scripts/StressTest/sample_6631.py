distance_covered_premise = 800
distance_covered_hypothesis = 500
speed_sandy = 15

# the hypothesis refers to the distance covered by Sandy, also mentioned in the premise
if distance_covered_hypothesis >= distance_covered_premise:
    # check if the distance in the hypothesis contradicts the premise's estimate of less than 'distance_covered_premise'
    label = "contradiction"
elif distance_covered_hypothesis < distance_covered_premise:
    # the premise gives only an estimate for the distance covered
    # any distance less than 'distance_covered_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
