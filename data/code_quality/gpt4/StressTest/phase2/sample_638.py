earnings_premise = 320
earnings_hypothesis = 320

# the hypothesis refers to Michael's earnings mentioned in the premise
if earnings_hypothesis >= earnings_premise:
    # check if the earnings in the hypothesis contradicts the earnings mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
