# Premise: Ganesh covers the distance from X to Y at an average speed of 54 Km/hr.
# Hypothesis: Ganesh covers the distance from X to Y at an average speed of 14 Km/hr.
# Golden Label: contradiction

speed_premise = 54
speed_hypothesis = 14

# the hypothesis talks about the speed covered by Ganesh from X to Y, which is also mentioned in the premise
if speed_hypothesis != speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # the speed in the hypothesis is the same as in the premise, so we can infer entailment
    label = "entailment"

print(label)

