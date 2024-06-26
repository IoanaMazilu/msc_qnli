earnings_premise = 9000
earnings_hypothesis = 9000

# the hypothesis refers to the earnings of 'he' and 'Rick' mentioned in the premise
if earnings_hypothesis >= earnings_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
