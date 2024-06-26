poll_premise = 0.52
poll_hypothesis = 0.52

# the hypothesis mentions the majority of those polled, which is also mentioned in the premise
if poll_hypothesis!= poll_premise:
    # check if the poll in the hypothesis contradicts the poll reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
