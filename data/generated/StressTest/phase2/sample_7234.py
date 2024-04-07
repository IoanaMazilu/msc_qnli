# Premise: Two twins sisters Sita and Geeta were standing back to back and suddenly they started running in opposite directions for less than 3 km each.
# Hypothesis: Two twins sisters Sita and Geeta were standing back to back and suddenly they started running in opposite directions for 2 km each.
# Golden Label: neutral

distance_premise = 3
distance_hypothesis = 2

# the hypothesis refers to the distance ran by the twins in the premise
if distance_hypothesis >= distance_premise:
    # check if the distance in the hypothesis contradicts the premise, which specifies 'less than 3 km'
    label = "contradiction"
else:
    # if the distance in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

