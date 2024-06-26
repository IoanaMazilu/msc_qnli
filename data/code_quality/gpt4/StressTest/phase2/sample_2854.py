earnings_premise = 463
earnings_hypothesis = 363

# the hypothesis refers to the earnings of Michael mentioned in the premise
if earnings_hypothesis >= earnings_premise:
    # check if the earnings in the hypothesis contradicts the estimate of less than 'earnings_premise' in the premise
    label = "contradiction"
else:
    # any earnings less than 'earnings_premise' is consistent with the premise, and hence the hypothesis can be entailed from the premise
    label = "entailment"

print(label)
