# Premise: Carl drove from his home to the beach at an average speed of 80 kilometers per hour and returned home by the same route at an average speed of 70 kilometers per hour.
# Hypothesis: Carl drove from his home to the beach at an average speed of 10 kilometers per hour and returned home by the same route at an average speed of 70 kilometers per hour.
# Golden Label: contradiction

speed_to_beach_premise = 80
speed_to_beach_hypothesis = 10
speed_home_premise = 70
speed_home_hypothesis = 70

# the hypothesis refers to the average speeds mentioned in the premise
if speed_to_beach_hypothesis != speed_to_beach_premise:
    # check if the speed to the beach in the hypothesis contradicts the speed to the beach reported in the premise
    label = "contradiction"
elif speed_home_hypothesis != speed_home_premise:
    # check if the speed home in the hypothesis contradicts the speed home reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

