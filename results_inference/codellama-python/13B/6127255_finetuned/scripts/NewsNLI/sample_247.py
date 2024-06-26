fine_premise = 8000
fine_hypothesis = 8000

# the hypothesis mentions the fine amount for Jessop, which is also mentioned in the premise
if fine_hypothesis!= fine_premise:
    # check if the fine amount in the hypothesis contradicts the fine amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
