earnings_premise = 810
earnings_hypothesis = 210

# the hypothesis refers to the earnings of Michael, which is also mentioned in the premise
if earnings_hypothesis >= earnings_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif earnings_hypothesis < earnings_premise:
    # if the hypothesis value is less than the premise, it is entailed by the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise, it is neutral
    label = "neutral"

print(label)
