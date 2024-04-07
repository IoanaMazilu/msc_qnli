# Premise: How many seconds does Sandy take to cover a distance of more than 300 meters, if Sandy runs at a speed of 18 km/hr?
# Hypothesis: How many seconds does Sandy take to cover a distance of 500 meters, if Sandy runs at a speed of 18 km/hr?
# Golden Label: neutral

distance_covered_premise = 300
distance_covered_hypothesis = 500
speed_sandy = 18

# the hypothesis talks about the distance covered and the speed which are also mentioned in the premise
if distance_covered_hypothesis <= distance_covered_premise:
    # check if the hypothesis value contradicts the premise's estimate of more than 'distance_covered_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance covered
    # any distance greater than 'distance_covered_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

