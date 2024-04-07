# Premise: If John runs in the speed of 9 km/hr from his house, in what time will he reach the park which is 300 m long from his house?
# Hypothesis: If John runs in the speed of 8 km/hr from his house, in what time will he reach the park which is 300 m long from his house?
# Golden Label: contradiction

speed_premise = 9
speed_hypothesis = 8
distance_premise = 300 / 1000  # convert to km
distance_hypothesis = 300 / 1000  # convert to km

# the premise and hypothesis both talk about John's speed and the distance to the park
if speed_hypothesis != speed_premise:
    # check if the speed in the hypothesis contradicts the speed indicated in the premise
    label = "contradiction"
elif distance_hypothesis != distance_premise:
    # check if the distance to the park in the hypothesis contradicts the distance mentioned in the premise
    label = "contradiction"
else:
    # the hypothesis does not contradict the premise, but it cannot be fully and explicitly entailed from the premise due to the different speeds
    label = "neutral"

print(label)

