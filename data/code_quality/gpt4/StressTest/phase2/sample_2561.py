tim_investment_premise = 700
jim_investment_premise = 300
tim_investment_hypothesis = 300
jim_investment_hypothesis = 300

# the hypothesis refers to the investments of Tim and Jim mentioned in the premise
if tim_investment_hypothesis != tim_investment_premise:
    # check if the investment of Tim in the hypothesis contradicts the investment of Tim in the premise
    label = "contradiction"
elif jim_investment_hypothesis != jim_investment_premise:
    # check if the investment of Jim in the hypothesis contradicts the investment of Jim in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
