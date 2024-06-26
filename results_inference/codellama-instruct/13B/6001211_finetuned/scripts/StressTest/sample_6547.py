distance_premise = 85
distance_hypothesis = 15

# the hypothesis refers to the distance between West-Town to East-Town mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)