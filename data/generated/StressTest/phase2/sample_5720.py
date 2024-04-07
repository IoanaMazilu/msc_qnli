# Premise: Ganesh covers the distance from X to Y at an average speed of 43 Km/hr.
# Hypothesis: Ganesh covers the distance from X to Y at an average speed of less than 43 Km/hr.
# Golden Label: contradiction

average_speed_premise = 43
average_speed_hypothesis = 43

# the hypothesis refers to the average speed from X to Y mentioned in the premise
if average_speed_hypothesis >= average_speed_premise:
    # check if the hypothesis value contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

