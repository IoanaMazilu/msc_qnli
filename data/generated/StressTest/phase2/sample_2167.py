# Premise: How many seconds does Sandy take to cover a distance of more than 200 meters, if Sandy runs at a speed of 18 km/hr?
# Hypothesis: How many seconds does Sandy take to cover a distance of 700 meters, if Sandy runs at a speed of 18 km/hr?
# Golden Label: neutral

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

