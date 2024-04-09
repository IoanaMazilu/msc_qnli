earnings_premise = 9000
earnings_hypothesis = 9000

# the hypothesis refers to the earnings mentioned in the premise
if earnings_hypothesis >= earnings_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif earnings_hypothesis < earnings_premise:
    # check if the hypothesis value is less than the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise, it is neutral
    label = "neutral"

print(label)
