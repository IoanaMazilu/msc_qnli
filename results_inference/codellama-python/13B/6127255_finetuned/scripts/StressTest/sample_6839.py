earnings_premise = 9000
earnings_hypothesis = 9000

# the hypothesis refers to the earnings mentioned in the premise
if earnings_hypothesis >= earnings_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, it can be entailed from the premise
    label = "entailment"

print(label)
