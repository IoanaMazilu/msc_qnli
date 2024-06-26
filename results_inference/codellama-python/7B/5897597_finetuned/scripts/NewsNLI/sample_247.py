fine_premise = 8000
fine_hypothesis = 8000

# the hypothesis mentions the fine that Jessop must pay, which is also mentioned in the premise
if fine_hypothesis!= fine_premise:
    # check if the fine in the hypothesis contradicts the fine reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
