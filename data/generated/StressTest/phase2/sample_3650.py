# Premise: Two twins sisters Sita and Geeta were standing back to back and suddenly they started running in opposite directions for 8 km each.
# Hypothesis: Two twins sisters Sita and Geeta were standing back to back and suddenly they started running in opposite directions for less than 8 km each.
# Golden Label: contradiction

distance_run_premise = 8
distance_run_hypothesis = 8

# the hypothesis is a statement about the distance the sisters ran, which is also in the premise
if distance_run_hypothesis >= distance_run_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

