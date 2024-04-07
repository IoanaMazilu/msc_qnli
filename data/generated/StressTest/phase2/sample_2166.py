# Premise: How many seconds does Sandy take to cover a distance of 700 meters, if Sandy runs at a speed of 18 km/hr?
# Hypothesis: How many seconds does Sandy take to cover a distance of more than 200 meters, if Sandy runs at a speed of 18 km/hr?
# Golden Label: entailment

distance_premise = 700
distance_hypothesis = 200
speed_premise = 18
speed_hypothesis = 18

# Both the premise and hypothesis refer to the same speed and a distance covered by Sandy
if speed_hypothesis != speed_premise:
    # Check if the speed of Sandy in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
elif distance_hypothesis > distance_premise:
    # Check if the distance in the hypothesis contradicts the distance covered by Sandy in the premise
    label = "contradiction"
elif distance_hypothesis == distance_premise:
    # If the distance in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"
else:
    # If the distance in the hypothesis is less than in the premise, but not contradicting it, we have a neutral relation
    label = "neutral"

print(label)

