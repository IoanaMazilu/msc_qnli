# Premise: Ganesh covers the distance from X to Y at an average speed of 43 Km/hr.
# Hypothesis: Ganesh covers the distance from X to Y at an average speed of less than 63 Km/hr.
# Golden Label: entailment

average_speed_premise = 43
average_speed_hypothesis = 63

# the hypothesis refers to the average speed mentioned in the premise
if average_speed_hypothesis <= average_speed_premise:
    # check if the speed 'average_speed_hypothesis' contradicts the speed in the premise
    label = "contradiction"
elif average_speed_premise > average_speed_hypothesis:
    # check if the speed in the premise contradicts the 'average_speed_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

