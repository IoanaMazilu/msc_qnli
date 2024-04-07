# Premise: 14000 in a business which he jointly owns with two other persons (James and Greg)
# Hypothesis: 24000 in a business which he jointly owns with two other persons (James and Greg)
# Golden Label: contradiction

business_investment_premise = 14000
business_investment_hypothesis = 24000

# the hypothesis refers to the value of investment in a business mentioned in the premise
if business_investment_hypothesis <= business_investment_premise:
    # check if the 'business_investment_hypothesis' contradicts the value of business investment in the premise
    label = "contradiction"
elif business_investment_hypothesis > business_investment_premise:
    # check if the 'business_investment_hypothesis' contradicts the value of business investment in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

