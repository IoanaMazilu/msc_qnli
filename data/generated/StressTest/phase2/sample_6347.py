# Premise: Mr Sharad started a business investing 50000.
# Hypothesis: Mr Sharad started a business investing less than 50000.
# Golden Label: contradiction

investment_premise = 50000
investment_hypothesis = 50000

# the hypothesis refers to the amount of investment made by Mr Sharad which is also mentioned in the premise
if investment_hypothesis >= investment_premise:
    # check if the hypothesis value contradicts the estimate of less than 'investment_premise'
    label = "contradiction"
else:
    # the premise clearly states the amount of investment by Mr Sharad
    # any amount less than 'investment_premise' contradicts the premise
    label = "contradiction"

print(label)

