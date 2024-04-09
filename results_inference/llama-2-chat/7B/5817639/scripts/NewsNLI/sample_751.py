andy_murray_premise = 1
andy_murray_hypothesis = 1

# the hypothesis mentions Andy Murray's match outcome, which is also referenced in the premise
if andy_murray_hypothesis!= andy_murray_premise:
    # check if the match outcome in the hypothesis contradicts the match outcome in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
