tim_investment_premise = 700
jim_investment_premise = 300
tim_investment_hypothesis = 300
jim_investment_hypothesis = 300

# The hypothesis refers to the investments of Tim and Jim mentioned in the premise
if tim_investment_hypothesis >= tim_investment_premise:
    # Check if the value in 'tim_investment_hypothesis' contradicts the investment of Tim in the premise
    label = "contradiction"
elif jim_investment_hypothesis != jim_investment_premise:
    # Check if the investment of Jim in the hypothesis contradicts the investment of Jim in the premise
    label = "contradiction"
else:
    # If the values in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)
