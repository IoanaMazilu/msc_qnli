investment_premise = 50000
investment_hypothesis = 50000

# the hypothesis refers to the amount of money Mr Sharad invested in his business, which is also mentioned in the premise
if investment_hypothesis >= investment_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, it can be entailed from the premise
    label = "entailment"

print(label)
