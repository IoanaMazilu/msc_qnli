# Premise: How many seconds does Sandy take to cover a distance of 600 meters, if Sandy runs at a speed of 15 km/hr?
# Hypothesis: How many seconds does Sandy take to cover a distance of less than 800 meters, if Sandy runs at a speed of 15 km/hr?
# Golden Label: entailment

distance_covered_premise = 600
distance_covered_hypothesis = 800
speed_sandy = 15

# the hypothesis refers to the distance covered and the speed of Sandy mentioned in the premise
if distance_covered_hypothesis <= distance_covered_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif speed_sandy != 15:
    # check if the speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

