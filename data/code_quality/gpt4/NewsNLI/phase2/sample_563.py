dead_not_from_india_premise = 4
dead_not_from_india_hypothesis = 4

# the hypothesis mentions the number of non-Indian dead, which is also mentioned in the premise
if dead_not_from_india_hypothesis != dead_not_from_india_premise:
    # check if the number of non-Indian dead in the hypothesis contradicts the number of non-Indian dead mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis number does not contradict the premise number, we can infer entailment
    label = "entailment"

print(label)
