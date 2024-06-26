earnings_premise = 358
earnings_hypothesis = 858

# the hypothesis refers to the earnings of Michael mentioned in the premise
if earnings_premise >= earnings_hypothesis:
    # check if 'earnings_premise' contradicts the estimate of less than 'earnings_hypothesis'
    label = "contradiction"
elif earnings_premise < earnings_hypothesis:
    # if 'earnings_premise' is less than 'earnings_hypothesis', we can infer entailment
    label = "entailment"

print(label)
