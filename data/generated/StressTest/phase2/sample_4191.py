# Premise: 1000, what is Isabella's capital?
# Hypothesis: less than 2000, what is Isabella's capital?
# Golden Label: entailment

capital_premise = 1000
capital_hypothesis = 2000

# the hypothesis talks about the amount of Isabella's capital, referenced also in the premise
if capital_premise >= capital_hypothesis:
    # check if the premise value contradicts the estimate of less than 'capital_hypothesis'
    label = "contradiction"
else:
    # the hypothesis gives only an estimate for the amount of Isabella's capital
    # any capital less than 'capital_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the hypothesis
    label = "neutral"

print(label)

