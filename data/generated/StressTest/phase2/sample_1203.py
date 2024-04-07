# Premise: Carl drove from his home to the beach at an average speed of 80 kilometers per hour and returned home by the same route at an average speed of 70 kilometers per hour.
# Hypothesis: Carl drove from his home to the beach at an average speed of more than 40 kilometers per hour and returned home by the same route at an average speed of 70 kilometers per hour.
# Golden Label: entailment

speed_to_beach_premise = 80
speed_to_beach_hypothesis = 40
speed_home_premise = 70
speed_home_hypothesis = 70

# the hypothesis refers to the average speed of Carl's trips mentioned in the premise
if speed_to_beach_premise <= speed_to_beach_hypothesis:
    # check if the estimate of 'speed_to_beach_hypothesis' contradicts the average speed to the beach in the premise
    label = "contradiction"
elif speed_home_hypothesis != speed_home_premise:
    # check if the average speed home in the hypothesis contradicts the average speed home reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

