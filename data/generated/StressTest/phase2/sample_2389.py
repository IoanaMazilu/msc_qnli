# Premise: less than 350, what is Belle's capital?
# Hypothesis: 250, what is Belle's capital?
# Golden Label: neutral

capital_premise = 350
capital_hypothesis = 250

# the hypothesis gives an estimate for Belle's capital, which is also referenced in the premise
if capital_hypothesis >= capital_premise:
    # check if the hypothesis value contradicts the estimate of less than 'capital_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Belle's capital
    # any capital less than 'capital_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

