# Premise: How many seconds does Sandy take to cover a distance of 500 meters, if Sandy runs at a speed of 18 km/hr?
# Hypothesis: How many seconds does Sandy take to cover a distance of more than 300 meters, if Sandy runs at a speed of 18 km/hr?
# Golden Label: entailment

distance_premise = 500
distance_hypothesis = 300
speed_premise = 18
speed_hypothesis = 18

# both the premise and hypothesis refer to Sandy's speed and the distance she covers
if speed_hypothesis != speed_premise:
    # check if the speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
elif distance_hypothesis > distance_premise:
    # check if the distance in the hypothesis contradicts the distance mentioned in the premise
    label = "contradiction"
else:
    # the premise gives a specific distance Sandy covers, while the hypothesis gives a lower bound
    # thus, the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from it either
    label = "neutral"

print(label)

