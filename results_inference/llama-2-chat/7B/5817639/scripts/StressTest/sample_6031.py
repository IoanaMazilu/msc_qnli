distance_premise = 8 / 2
distance_hypothesis = 1 / 2

# the hypothesis talks about the distance traveled by Maria during a car trip
if distance_hypothesis <= distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance traveled in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the distance traveled, and the hypothesis value is consistent with it
    label = "entailment"

print(label)
