distance_premise = 200
distance_hypothesis = 700
speed = 18

# the hypothesis talks about the time Sandy would take to cover a certain distance at a certain speed,
# which is also referenced in the premise

if distance_hypothesis <= distance_premise:
    # check if the hypothesis distance contradicts the premise's estimate of more than 'distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance greater than 'distance_premise' at 'speed' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
