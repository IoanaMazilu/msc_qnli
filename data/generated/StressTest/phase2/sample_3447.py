# Premise: Ganesh covers the distance from X to Y at an average speed of 60 Km/hr.
# Hypothesis: Ganesh covers the distance from X to Y at an average speed of more than 50 Km/hr.
# Golden Label: entailment

average_speed_premise = 60
average_speed_hypothesis = 50

# the hypothesis refers to the average speed of Ganesh mentioned in the premise
if average_speed_premise <= average_speed_hypothesis:
    # check if the average speed in the hypothesis contradicts the average speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

