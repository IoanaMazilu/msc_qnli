# Premise: Ganesh covers the distance from X to Y at an average speed of 54 Km/hr.
# Hypothesis: Ganesh covers the distance from X to Y at an average speed of more than 44 Km/hr.
# Golden Label: entailment

avg_speed_premise = 54
avg_speed_hypothesis = 44

# the hypothesis refers to the average speed of Ganesh from X to Y, mentioned in the premise
if avg_speed_premise <= avg_speed_hypothesis:
    # check if the 'avg_speed_hypothesis' contradicts the average speed in the premise
    label = "contradiction"
else:
    # if the speed value in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

