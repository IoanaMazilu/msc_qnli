distance_premise = 1 / 2
distance_hypothesis = 7 / 2

# the hypothesis refers to the distance traveled by Maria in the premise
if distance_hypothesis >= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance traveled in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the distance traveled, and the hypothesis provides a different estimate
    # any distance traveled greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
