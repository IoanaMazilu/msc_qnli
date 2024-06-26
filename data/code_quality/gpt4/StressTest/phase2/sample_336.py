earnings_premise = 9000
earnings_hypothesis = 4000

# the hypothesis refers to the total earnings mentioned in the premise
if earnings_hypothesis >= earnings_premise:
    # check if the estimate of 'earnings_hypothesis' contradicts the earnings in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise amount, we can infer entailment
    label = "entailment"

print(label)