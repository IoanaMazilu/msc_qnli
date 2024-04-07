# Premise: Ganesh covers the distance from X to Y at an average speed of 43 Km/hr.
# Hypothesis: Ganesh covers the distance from X to Y at an average speed of less than 83 Km/hr.
# Golden Label: entailment

average_speed_premise = 43
average_speed_hypothesis = 83

# the hypothesis refers to the average speed of Ganesh from X to Y mentioned in the premise
if average_speed_premise >= average_speed_hypothesis:
    # check if the actual speed of Ganesh contradicts the estimate of 'less than average_speed_hypothesis'
    label = "contradiction"
else:
    # the premise gives the exact speed of Ganesh, any speed less than 'average_speed_hypothesis' does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

