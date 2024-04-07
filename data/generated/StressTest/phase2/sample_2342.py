# Premise: How many seconds does Sandy take to cover a distance of 600 meters, if Sandy runs at a speed of 15 km/hr?
# Hypothesis: How many seconds does Sandy take to cover a distance of less than 600 meters, if Sandy runs at a speed of 15 km/hr?
# Golden Label: contradiction

distance_premise = 600
distance_hypothesis = 600
speed_premise = 15
speed_hypothesis = 15

# the hypothesis mentions the speed and distance covered by Sandy, which is also addressed in the premise
if speed_hypothesis != speed_premise:
    # check if the speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
elif distance_hypothesis >= distance_premise:
    # check if the distance in the hypothesis contradicts the premise's claim that Sandy covers 'distance_premise' meters
    label = "contradiction"
else:
    # the premise gives only an exact distance that Sandy covers
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

