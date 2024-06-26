capital_premise = 2000
capital_hypothesis = 1000

# the hypothesis refers to a possible value of Isabella's capital, which is also talked about in the premise
if capital_hypothesis >= capital_premise:
    # check if the hypothesis value contradicts the estimate of 'less than capital_premise'
    label = "contradiction"
elif capital_hypothesis < capital_premise:
    # any capital value less than 'capital_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
