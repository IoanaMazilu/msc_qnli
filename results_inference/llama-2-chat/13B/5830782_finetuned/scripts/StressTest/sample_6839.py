earnings_premise = 9000
earnings_hypothesis = 9000

# the hypothesis refers to the total earnings of 'he' and 'Rick' mentioned in the premise
if earnings_hypothesis >= earnings_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
