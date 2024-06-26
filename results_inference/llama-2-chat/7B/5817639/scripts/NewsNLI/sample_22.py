poll_premise = 0.5
poll_hypothesis = 0.5

# the hypothesis mentions the poll results, which are also referenced in the premise
if poll_hypothesis!= poll_premise:
    # check if the poll results in the hypothesis contradict the poll results in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
