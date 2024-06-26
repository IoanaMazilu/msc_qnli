business_investment_premise = 50000
business_investment_hypothesis = 50000

# the hypothesis refers to the business investment made by Mr Sharad, mentioned in the premise
if business_investment_hypothesis >= business_investment_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
