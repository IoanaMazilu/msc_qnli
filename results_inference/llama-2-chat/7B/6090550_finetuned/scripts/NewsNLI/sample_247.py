fine_premise = 8000
fine_hypothesis = 8000

# the hypothesis mentions the amount of the fine, which is also mentioned in the premise
if fine_hypothesis!= fine_premise:
    # check if the fine amount in the hypothesis contradicts the fine amount in the premise
    label = "contradiction"
else:
    # if the fine amount in the hypothesis does not contradict the fine amount in the premise, we can infer entailment
    label = "entailment"

print(label)