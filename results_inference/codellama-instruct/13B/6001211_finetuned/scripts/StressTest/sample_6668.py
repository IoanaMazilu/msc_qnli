work_completion_premise = 20
work_completion_hypothesis = 50

# the hypothesis refers to the completion time of work by Kamal mentioned in the premise
if work_completion_hypothesis!= work_completion_premise:
    # check if the completion time in the hypothesis contradicts the completion time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
