# Premise: Two twins sisters Sita and Geeta were standing back to back and suddenly they started running in opposite directions for 12 km each.
# Hypothesis: Two twins sisters Sita and Geeta were standing back to back and suddenly they started running in opposite directions for less than 12 km each.
# Golden Label: contradiction

distance_run_premise = 12
distance_run_hypothesis = 12

# the hypothesis refers to the distance run by the sisters mentioned in the premise
if distance_run_hypothesis >= distance_run_premise:
    # check if the 'distance_run_hypothesis' contradicts the distance run in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

