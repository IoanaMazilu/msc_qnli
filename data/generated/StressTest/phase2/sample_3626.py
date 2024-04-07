# Premise: Ganesh covers the distance from X to Y at an average speed of 43 Km/hr.
# Hypothesis: Ganesh covers the distance from X to Y at an average speed of 53 Km/hr.
# Golden Label: contradiction

average_speed_premise = 43
average_speed_hypothesis = 53

# the hypothesis discusses the average speed of Ganesh from X to Y, which is also mentioned in the premise
if average_speed_hypothesis != average_speed_premise:
    # check if the average speed in the hypothesis contradicts the average speed mentioned in the premise
    label = "contradiction"
else:
    # if the average speeds in both the premise and hypothesis are the same, we can infer entailment
    label = "entailment"

print(label)

