distance_covered_premise = 500
distance_covered_hypothesis = 800
speed_premise = 15
speed_hypothesis = 15

# The hypothesis refers to the distance covered by Sandy and her speed mentioned in the premise
if speed_hypothesis != speed_premise:
    # Check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif distance_covered_hypothesis < distance_covered_premise:
    # Check if the distance in the hypothesis contradicts the distance covered by Sandy in the premise
    label = "contradiction"
elif distance_covered_hypothesis > distance_covered_premise:
    # Check if the distance in the hypothesis entails the distance covered by Sandy in the premise
    label = "entailment"
else:
    # If the hypothesis values and estimates do not contradict or entail the premise ones,
    # we can infer that the relationship is neutral
    label = "neutral"

print(label)
