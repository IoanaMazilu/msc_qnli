earnings_premise = 9000
earnings_hypothesis = 9000

# the hypothesis refers to the number of earnings mentioned in the premise
if earnings_hypothesis < earnings_premise:
    # check if the estimate of 'earnings_hypothesis' contradicts the number of earnings in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
