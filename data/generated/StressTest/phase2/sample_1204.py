# Premise: Carl drove from his home to the beach at an average speed of more than 40 kilometers per hour and returned home by the same route at an average speed of 70 kilometers per hour.
# Hypothesis: Carl drove from his home to the beach at an average speed of 80 kilometers per hour and returned home by the same route at an average speed of 70 kilometers per hour.
# Golden Label: neutral

speed_to_beach_premise = 40
speed_to_beach_hypothesis = 80
speed_home_premise = 70
speed_home_hypothesis = 70

# the hypothesis refers to the same journeys made by Carl as mentioned in the premise
if speed_to_beach_hypothesis <= speed_to_beach_premise:
    # check if the speed 'speed_to_beach_hypothesis' contradicts the estimate of more than 'speed_to_beach_premise'
    label = "contradiction"
elif speed_home_hypothesis != speed_home_premise:
    # check if the speed home in the hypothesis contradicts the speed home in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed to the beach
    # any speed greater than 'speed_to_beach_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

