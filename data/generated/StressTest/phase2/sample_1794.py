# Premise: Two twins sisters Sita and Geeta were standing back to back and suddenly they started running in opposite directions for 6 km each.
# Hypothesis: Two twins sisters Sita and Geeta were standing back to back and suddenly they started running in opposite directions for less than 8 km each.
# Golden Label: entailment

distance_run_by_each_sister_premise = 6
distance_run_by_each_sister_hypothesis = 8

# the hypothesis refers to the distance run by Sita and Geeta, which is also mentioned in the premise
if distance_run_by_each_sister_hypothesis < distance_run_by_each_sister_premise:
    # check if the hypothesis contradicts the distance run by each sister as stated in the premise
    label = "contradiction"
elif distance_run_by_each_sister_hypothesis > distance_run_by_each_sister_premise:
    # check if the hypothesis entails more distance run by each sister than stated in the premise
    label = "neutral"
else:
    # if the hypothesis values do not contradict or entail more than the premise ones, we can infer entailment
    label = "entailment"

print(label)

