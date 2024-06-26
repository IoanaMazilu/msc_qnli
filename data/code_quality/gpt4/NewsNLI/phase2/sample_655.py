company_contribution_premise = 17.5
total_cost_premise = 36
total_cost_hypothesis = 36

# the hypothesis implies that Microsoft is paying for about half of the total cost of the project
# this is the same as the premise, which states that the company is contributing a little less than half the total cost
if company_contribution_premise / total_cost_premise >= 0.5:
    # check if the contribution of the company in the premise is actually more than half of the total cost
    label = "contradiction"
elif company_contribution_premise != total_cost_hypothesis / 2:
    # check if the company's contribution from the premise contradicts the implied contribution in the hypothesis
    label = "neutral"
else:
    # if the company's contribution in the premise does not contradict the implied contribution in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
