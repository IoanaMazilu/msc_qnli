# Premise: Ganesh covers the distance from X to Y at an average speed of 60 Km/hr.
# Hypothesis: Ganesh covers the distance from X to Y at an average speed of less than 60 Km/hr.
# Golden Label: contradiction

avg_speed_premise = 60
avg_speed_hypothesis = 60

# The hypothesis refers to the average speed of Ganesh mentioned in the premise
if avg_speed_hypothesis >= avg_speed_premise:
    # Check if the 'avg_speed_hypothesis' contradicts the average speed in the premise
    label = "contradiction"
else:
    # If the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

