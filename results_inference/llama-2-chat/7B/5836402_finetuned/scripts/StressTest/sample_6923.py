earnings_premise = 210
earnings_hypothesis = 210

# the hypothesis refers to the earnings of Michael mentioned in the premise
if earnings_hypothesis <= earnings_premise:
    # check if the hypothesis value contradicts the earnings in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the earnings in the premise, we can infer entailment
    label = "entailment"

print(label)
