# Premise: Ganesh covers the distance from X to Y at an average speed of 44 Km/hr.
# Hypothesis: Ganesh covers the distance from X to Y at an average speed of more than 14 Km/hr.
# Golden Label: entailment

average_speed_premise = 44
average_speed_hypothesis = 14

# the hypothesis refers to the average speed of Ganesh from X to Y mentioned in the premise
if average_speed_premise <= average_speed_hypothesis:
    # check if the estimate of 'average_speed_hypothesis' contradicts the speed given in the premise
    label = "contradiction"
else:
    # if the hypothesis speed is less than the premise speed, we can infer entailment
    label = "entailment"

print(label)

