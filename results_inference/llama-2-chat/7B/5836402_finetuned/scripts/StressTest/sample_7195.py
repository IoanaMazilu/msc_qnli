coverage_distance_premise = 6 * 24 + 1
coverage_distance_hypothesis = 7 * 24 + 1

# the hypothesis refers to the distance covered by the train, which is also mentioned in the premise
if coverage_distance_hypothesis <= coverage_distance_premise:
    # check if the hypothesis value contradicts the estimate of more than 'coverage_distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance greater than 'coverage_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
