distance_premise = 52
distance_hypothesis = 12

# the hypothesis refers to the distance covered by each twin sister
if distance_hypothesis <= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance covered by each twin sister in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance covered by each twin sister
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
