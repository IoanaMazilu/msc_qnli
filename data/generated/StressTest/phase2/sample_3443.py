# Premise: How many seconds does Sandy take to cover a distance of 600 meters, if Sandy runs at a speed of 18 km/hr?
# Hypothesis: How many seconds does Sandy take to cover a distance of less than 600 meters, if Sandy runs at a speed of 18 km/hr?
# Golden Label: contradiction

distance_premise = 600
distance_hypothesis = 600
speed_premise = 18
speed_hypothesis = 18

# the hypothesis refers to the same speed and distance values as the premise
if speed_hypothesis != speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif distance_hypothesis >= distance_premise:
    # check if the distance in the hypothesis contradicts the premise that the distance is less than 'distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance covered
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

