# Premise: Four months later Mr Praveen joined the business by investing 90000.
# Hypothesis: Four months later Mr Praveen joined the business by investing more than 30000.
# Golden Label: entailment

investment_premise = 90000
investment_hypothesis = 30000

# the hypothesis talks about the amount Mr Praveen invested in the business, referenced also in the premise
if investment_hypothesis >= investment_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)

