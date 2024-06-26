poll_obama_premise = 0.5
poll_obama_hypothesis = 0.5

# the hypothesis mentions Obama's lead in Ohio and two other battleground states, which is also mentioned in the premise
if poll_obama_hypothesis == poll_obama_premise:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates contradict the premise values, we can infer contradiction
    label = "contradiction"

print(label)
