paid_premise = 100000
paid_hypothesis = 100000

# the hypothesis mentions the amount paid by the passenger, which is also mentioned in the premise
if paid_hypothesis!= paid_premise:
    # check if the amount paid in the hypothesis contradicts the amount paid reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
