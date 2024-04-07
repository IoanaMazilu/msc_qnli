# Premise: How many seconds does Sandy take to cover a distance of less than 800 meters, if Sandy runs at a speed of 15 km/hr?
# Hypothesis: How many seconds does Sandy take to cover a distance of 600 meters, if Sandy runs at a speed of 15 km/hr?
# Golden Label: neutral

distance_covered_premise = 800
distance_covered_hypothesis = 600
speed_sandy_premise = 15
speed_sandy_hypothesis = 15

# the hypothesis talks about the time Sandy takes to cover a certain distance at a certain speed
# these are also referred to in the premise
if distance_covered_hypothesis >= distance_covered_premise:
    # check if the distance in the hypothesis contradicts the premise estimate of less than 'distance_covered_premise'
    label = "contradiction"
elif speed_sandy_hypothesis != speed_sandy_premise:
    # check if the speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance covered
    # any distance less than 'distance_covered_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

