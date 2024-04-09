business_investment_premise = 50000
business_investment_hypothesis = 10000

# the hypothesis refers to the amount Mr Sharad invested in the business, which is also mentioned in the premise
if business_investment_premise <= business_investment_hypothesis:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
