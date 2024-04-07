# Premise: Two twins sisters Sita and Geeta were standing back to back and suddenly they started running in opposite directions for 10 km each.
# Hypothesis: Two twins sisters Sita and Geeta were standing back to back and suddenly they started running in opposite directions for more than 10 km each.
# Golden Label: contradiction

distance_run_by_sisters_premise = 10
distance_run_by_sisters_hypothesis = 10

# the hypothesis talks about the distance run by the sisters, which is also mentioned in the premise
if distance_run_by_sisters_hypothesis > distance_run_by_sisters_premise:
    # check if the hypothesis value contradicts the distance run by the sisters in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

